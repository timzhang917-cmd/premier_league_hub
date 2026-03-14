from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MatchForm
from .models import Match


def index(request):
    if request.method == "POST" and not request.user.is_authenticated:
        return redirect_to_login(request.get_full_path())

    form = MatchForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Match saved successfully.")
        return redirect("match_results_index")

    matches = Match.objects.select_related("home_team", "away_team").all()
    context = {
        "form": form,
        "matches": matches,
        "finished_count": matches.filter(status=Match.Status.FINISHED).count(),
        "scheduled_count": matches.filter(status=Match.Status.SCHEDULED).count(),
    }
    return render(request, "match_results/index.html", context)


@login_required
def edit_match(request, pk):
    match = get_object_or_404(Match.objects.select_related("home_team", "away_team"), pk=pk)
    form = MatchForm(request.POST or None, instance=match)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Match updated successfully.")
        return redirect("match_results_index")

    return render(
        request,
        "match_results/form.html",
        {
            "form": form,
            "match": match,
            "page_title": "Edit Match",
            "submit_label": "Save Changes",
        },
    )


@login_required
def delete_match(request, pk):
    match = get_object_or_404(Match.objects.select_related("home_team", "away_team"), pk=pk)
    if request.method == "POST":
        match.delete()
        messages.success(request, "Match deleted successfully.")
        return redirect("match_results_index")

    return render(request, "match_results/confirm_delete.html", {"match": match})
