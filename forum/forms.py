from django import forms

from teams.models import Team

from .models import Post


class PostForm(forms.ModelForm):
    team = forms.ModelChoiceField(
        queryset=Team.objects.order_by("name"),
        label="Team",
        empty_label="Select a team...",
        help_text="Each discussion post must be linked to one team.",
        widget=forms.Select(
            attrs={
                "class": "form-select",
                "required": True,
                "aria-describedby": "teamHelp",
            }
        ),
        error_messages={"required": "Please select a team."},
    )
    title = forms.CharField(
        label="Title",
        min_length=5,
        max_length=200,
        help_text="Use a short, clear title (min 5 characters, max 200).",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "e.g., What do you think about Arsenal's tactics today?",
                "required": True,
                "minlength": 5,
                "maxlength": 200,
                "autocomplete": "off",
                "aria-describedby": "titleHelp",
            }
        ),
        error_messages={
            "required": "Please enter a title.",
            "min_length": "Title is too short (min 5 characters).",
            "max_length": "Title is too long (max 200 characters).",
        },
    )
    content = forms.CharField(
        label="Content",
        min_length=20,
        help_text="Write your opinion (min 20 characters).",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 7,
                "placeholder": "Write your thoughts here (min 20 characters)...",
                "required": True,
                "minlength": 20,
                "aria-describedby": "contentHelp",
            }
        ),
        error_messages={
            "required": "Please enter your content.",
            "min_length": "Content is too short (min 20 characters).",
        },
    )

    class Meta:
        model = Post
        fields = ["team", "title", "content"]

    def clean_title(self):
        return (self.cleaned_data.get("title") or "").strip()

    def clean_content(self):
        return (self.cleaned_data.get("content") or "").strip()
