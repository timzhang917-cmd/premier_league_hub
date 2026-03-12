from django import forms

from .models import Match


class MatchForm(forms.ModelForm):
    match_date = forms.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(format="%Y-%m-%dT%H:%M", attrs={"type": "datetime-local"}),
    )

    class Meta:
        model = Match
        fields = ["home_team", "away_team", "match_date", "status", "home_score", "away_score"]
        widgets = {
            "status": forms.Select(),
            "home_score": forms.NumberInput(attrs={"min": 0, "placeholder": "Home goals"}),
            "away_score": forms.NumberInput(attrs={"min": 0, "placeholder": "Away goals"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ("home_team", "away_team"):
            self.fields[field_name].queryset = self.fields[field_name].queryset.order_by("name")
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")

    def clean(self):
        cleaned_data = super().clean()
        home_team = cleaned_data.get("home_team")
        away_team = cleaned_data.get("away_team")
        status = cleaned_data.get("status")
        home_score = cleaned_data.get("home_score")
        away_score = cleaned_data.get("away_score")

        if home_team and away_team and home_team == away_team:
            raise forms.ValidationError("Please choose two different teams.")

        if status == Match.Status.FINISHED:
            if home_score is None or away_score is None:
                raise forms.ValidationError("Finished matches need both scores.")
        elif home_score is not None or away_score is not None:
            raise forms.ValidationError("Only finished matches can include scores.")

        return cleaned_data
