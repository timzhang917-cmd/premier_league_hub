from django.db import migrations


def seed_teams(apps, schema_editor):
    Team = apps.get_model("teams", "Team")
    teams = [
        {
            "name": "Arsenal",
            "short_name": "ARS",
            "stadium": "Emirates Stadium",
            "founded_year": 1886,
            "description": "Arsenal Football Club, based in London, is one of the traditional powerhouses of the Premier League.",
            "logo_filename": "asenna.jpg",
        },
        {
            "name": "Aston Villa",
            "short_name": "AVL",
            "stadium": "Villa Park",
            "founded_year": 1874,
            "description": "Aston Villa FC, from Birmingham, is one of England's oldest and most decorated clubs.",
            "logo_filename": "weila.jpg",
        },
        {
            "name": "Chelsea",
            "short_name": "CHE",
            "stadium": "Stamford Bridge",
            "founded_year": 1905,
            "description": "Chelsea FC, based in London, is a leading Premier League and European side.",
            "logo_filename": "qieerxi.jpg",
        },
        {
            "name": "Crystal Palace",
            "short_name": "CRY",
            "stadium": "Selhurst Park",
            "founded_year": 1905,
            "description": "Crystal Palace FC is a London club with a strong identity and loyal support.",
            "logo_filename": "shuijing.jpg",
        },
        {
            "name": "Liverpool",
            "short_name": "LIV",
            "stadium": "Anfield",
            "founded_year": 1892,
            "description": "Liverpool FC, from Merseyside, is one of England's most successful clubs.",
            "logo_filename": "liwupu.png",
        },
        {
            "name": "Manchester City",
            "short_name": "MCI",
            "stadium": "Etihad Stadium",
            "founded_year": 1880,
            "description": "Manchester City FC has become a dominant force in the Premier League and in European competition.",
            "logo_filename": "manc.jpg",
        },
        {
            "name": "Manchester United",
            "short_name": "MUN",
            "stadium": "Old Trafford",
            "founded_year": 1878,
            "description": "Manchester United FC is one of the world's most famous and successful clubs.",
            "logo_filename": "manu.jpg",
        },
        {
            "name": "Tottenham Hotspur",
            "short_name": "TOT",
            "stadium": "Tottenham Hotspur Stadium",
            "founded_year": 1882,
            "description": "Tottenham Hotspur, from North London, is a historic top-flight club.",
            "logo_filename": "reci.jpg",
        },
        {
            "name": "West Ham United",
            "short_name": "WHU",
            "stadium": "London Stadium",
            "founded_year": 1895,
            "description": "West Ham United FC is an East London club with a rich tradition and passionate fanbase.",
            "logo_filename": "xihan.jpg",
        },
    ]

    for team in teams:
        Team.objects.update_or_create(name=team["name"], defaults=team)


def unseed_teams(apps, schema_editor):
    Team = apps.get_model("teams", "Team")
    Team.objects.filter(
        name__in=[
            "Arsenal",
            "Aston Villa",
            "Chelsea",
            "Crystal Palace",
            "Liverpool",
            "Manchester City",
            "Manchester United",
            "Tottenham Hotspur",
            "West Ham United",
        ]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_teams, unseed_teams),
    ]
