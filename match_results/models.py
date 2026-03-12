from django.core.exceptions import ValidationError
from django.db import models

from teams.models import Team


class Match(models.Model):
    class Status(models.TextChoices):
        SCHEDULED = "scheduled", "Scheduled"
        FINISHED = "finished", "Finished"
        POSTPONED = "postponed", "Postponed"

    home_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="home_matches",
    )
    away_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="away_matches",
    )
    match_date = models.DateTimeField()
    home_score = models.PositiveSmallIntegerField(blank=True, null=True)
    away_score = models.PositiveSmallIntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SCHEDULED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-match_date", "-id"]

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"

    def clean(self):
        if self.home_team_id and self.home_team_id == self.away_team_id:
            raise ValidationError("Home team and away team must be different.")

        if self.status == self.Status.FINISHED:
            if self.home_score is None or self.away_score is None:
                raise ValidationError("Finished matches require both scores.")
        elif self.home_score is not None or self.away_score is not None:
            raise ValidationError("Only finished matches can store final scores.")

    @property
    def scoreline(self):
        if self.home_score is None or self.away_score is None:
            return "vs"
        return f"{self.home_score} - {self.away_score}"
