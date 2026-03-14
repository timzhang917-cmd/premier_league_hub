from django.contrib import admin

from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "short_name", "stadium", "founded_year", "created_at")
    search_fields = ("name", "short_name", "stadium")
