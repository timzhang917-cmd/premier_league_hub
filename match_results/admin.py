from django.contrib import admin

from .models import Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("home_team", "away_team", "match_date", "status", "home_score", "away_score")
    list_filter = ("status", "match_date")
    search_fields = ("home_team__name", "away_team__name")
    autocomplete_fields = ("home_team", "away_team")
