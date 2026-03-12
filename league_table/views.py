from django.shortcuts import render

from match_results.models import Match
from teams.models import Team


def index(request):
    teams = list(Team.objects.all())
    finished_matches = list(
        Match.objects.select_related("home_team", "away_team")
        .filter(status=Match.Status.FINISHED)
        .order_by("match_date", "id")
    )
    upcoming_matches = (
        Match.objects.select_related("home_team", "away_team")
        .exclude(status=Match.Status.FINISHED)
        .order_by("match_date", "id")[:5]
    )

    standings = []
    rows_by_team_id = {}
    for team in teams:
        row = {
            "team": team,
            "played": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "goals_for": 0,
            "goals_against": 0,
            "goal_difference": 0,
            "points": 0,
        }
        rows_by_team_id[team.id] = row
        standings.append(row)

    for match in finished_matches:
        home_row = rows_by_team_id.get(match.home_team_id)
        away_row = rows_by_team_id.get(match.away_team_id)
        if home_row is None or away_row is None:
            continue

        home_row["played"] += 1
        away_row["played"] += 1
        home_row["goals_for"] += match.home_score
        home_row["goals_against"] += match.away_score
        away_row["goals_for"] += match.away_score
        away_row["goals_against"] += match.home_score

        if match.home_score > match.away_score:
            home_row["won"] += 1
            away_row["lost"] += 1
            home_row["points"] += 3
        elif match.home_score < match.away_score:
            away_row["won"] += 1
            home_row["lost"] += 1
            away_row["points"] += 3
        else:
            home_row["drawn"] += 1
            away_row["drawn"] += 1
            home_row["points"] += 1
            away_row["points"] += 1

    standings.sort(
        key=lambda row: (
            -row["points"],
            -(row["goals_for"] - row["goals_against"]),
            -row["goals_for"],
            row["team"].name,
        )
    )

    for position, row in enumerate(standings, start=1):
        row["position"] = position
        row["goal_difference"] = row["goals_for"] - row["goals_against"]

    return render(
        request,
        "league_table/index.html",
        {
            "standings": standings,
            "finished_match_count": len(finished_matches),
            "team_count": len(teams),
            "upcoming_matches": upcoming_matches,
        },
    )
