from django.db import migrations


DEFAULT_TEAMS = [
    {"name": "Arsenal", "short_name": "ARS"},
    {"name": "Liverpool", "short_name": "LIV"},
    {"name": "Manchester City", "short_name": "MCI"},
    {"name": "Manchester United", "short_name": "MUN"},
    {"name": "Chelsea", "short_name": "CHE"},
    {"name": "Tottenham Hotspur", "short_name": "TOT"},
    {"name": "Crystal Palace", "short_name": "CRY"},
    {"name": "Aston Villa", "short_name": "AVL"},
    {"name": "West Ham United", "short_name": "WHU"},
]


def seed_forum_teams(apps, schema_editor):
    Team = apps.get_model("teams", "Team")
    for team in DEFAULT_TEAMS:
        Team.objects.update_or_create(
            name=team["name"],
            defaults={"short_name": team["short_name"]},
        )


def unseed_forum_teams(apps, schema_editor):
    Team = apps.get_model("teams", "Team")
    Team.objects.filter(name__in=[team["name"] for team in DEFAULT_TEAMS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0002_seed_teams"),
    ]

    operations = [
        migrations.RunPython(seed_forum_teams, unseed_forum_teams),
    ]
