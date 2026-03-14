from datetime import datetime, timezone

from django.db import migrations


def seed_matches(apps, schema_editor):
    Match = apps.get_model("match_results", "Match")
    Team = apps.get_model("teams", "Team")

    team_ids = {team.name: team.id for team in Team.objects.all()}
    matches = [
        {
            "home_team_id": team_ids["Arsenal"],
            "away_team_id": team_ids["Chelsea"],
            "match_date": datetime(2026, 2, 20, 19, 30, tzinfo=timezone.utc),
            "home_score": 2,
            "away_score": 1,
            "status": "finished",
        },
        {
            "home_team_id": team_ids["Liverpool"],
            "away_team_id": team_ids["West Ham United"],
            "match_date": datetime(2026, 2, 22, 16, 0, tzinfo=timezone.utc),
            "home_score": 3,
            "away_score": 1,
            "status": "finished",
        },
        {
            "home_team_id": team_ids["Manchester City"],
            "away_team_id": team_ids["Tottenham Hotspur"],
            "match_date": datetime(2026, 2, 28, 17, 30, tzinfo=timezone.utc),
            "home_score": 1,
            "away_score": 1,
            "status": "finished",
        },
        {
            "home_team_id": team_ids["Aston Villa"],
            "away_team_id": team_ids["Crystal Palace"],
            "match_date": datetime(2026, 3, 2, 20, 0, tzinfo=timezone.utc),
            "home_score": 2,
            "away_score": 0,
            "status": "finished",
        },
        {
            "home_team_id": team_ids["Manchester United"],
            "away_team_id": team_ids["Arsenal"],
            "match_date": datetime(2026, 3, 5, 20, 0, tzinfo=timezone.utc),
            "home_score": 2,
            "away_score": 2,
            "status": "finished",
        },
        {
            "home_team_id": team_ids["Chelsea"],
            "away_team_id": team_ids["Liverpool"],
            "match_date": datetime(2026, 3, 15, 16, 30, tzinfo=timezone.utc),
            "home_score": None,
            "away_score": None,
            "status": "scheduled",
        },
        {
            "home_team_id": team_ids["West Ham United"],
            "away_team_id": team_ids["Aston Villa"],
            "match_date": datetime(2026, 3, 16, 19, 45, tzinfo=timezone.utc),
            "home_score": None,
            "away_score": None,
            "status": "scheduled",
        },
        {
            "home_team_id": team_ids["Tottenham Hotspur"],
            "away_team_id": team_ids["Manchester City"],
            "match_date": datetime(2026, 3, 18, 20, 0, tzinfo=timezone.utc),
            "home_score": None,
            "away_score": None,
            "status": "postponed",
        },
        {
            "home_team_id": team_ids["Crystal Palace"],
            "away_team_id": team_ids["Manchester United"],
            "match_date": datetime(2026, 3, 20, 19, 30, tzinfo=timezone.utc),
            "home_score": None,
            "away_score": None,
            "status": "scheduled",
        },
    ]

    for match in matches:
        Match.objects.update_or_create(
            home_team_id=match["home_team_id"],
            away_team_id=match["away_team_id"],
            match_date=match["match_date"],
            defaults=match,
        )


def unseed_matches(apps, schema_editor):
    Match = apps.get_model("match_results", "Match")
    Match.objects.filter(
        match_date__in=[
            datetime(2026, 2, 20, 19, 30, tzinfo=timezone.utc),
            datetime(2026, 2, 22, 16, 0, tzinfo=timezone.utc),
            datetime(2026, 2, 28, 17, 30, tzinfo=timezone.utc),
            datetime(2026, 3, 2, 20, 0, tzinfo=timezone.utc),
            datetime(2026, 3, 5, 20, 0, tzinfo=timezone.utc),
            datetime(2026, 3, 15, 16, 30, tzinfo=timezone.utc),
            datetime(2026, 3, 16, 19, 45, tzinfo=timezone.utc),
            datetime(2026, 3, 18, 20, 0, tzinfo=timezone.utc),
            datetime(2026, 3, 20, 19, 30, tzinfo=timezone.utc),
        ]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0002_seed_teams"),
        ("match_results", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_matches, unseed_matches),
    ]
