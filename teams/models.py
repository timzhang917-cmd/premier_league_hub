from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=120, unique=True)
    short_name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.short_name or self.name
