from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=20, unique=True)
    stadium = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField()
    description = models.TextField()
    logo_filename = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
