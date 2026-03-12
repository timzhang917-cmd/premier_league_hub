import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Match",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("match_date", models.DateTimeField()),
                ("home_score", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("away_score", models.PositiveSmallIntegerField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("scheduled", "Scheduled"),
                            ("finished", "Finished"),
                            ("postponed", "Postponed"),
                        ],
                        default="scheduled",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "away_team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="away_matches",
                        to="teams.team",
                    ),
                ),
                (
                    "home_team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="home_matches",
                        to="teams.team",
                    ),
                ),
            ],
            options={"ordering": ["-match_date", "-id"]},
        ),
    ]
