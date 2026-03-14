from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from teams.models import Team

from .forms import PostForm
from .models import Post


def forum_list(request):
    q = (request.GET.get("q") or "").strip()
    team_param = (request.GET.get("team") or "").strip()

    posts = Post.objects.select_related("author", "team")

    if q:
        posts = posts.filter(
            Q(title__icontains=q)
            | Q(content__icontains=q)
            | Q(author__username__icontains=q)
            | Q(team__name__icontains=q)
        )

    selected_team_id = None
    if team_param.isdigit():
        selected_team_id = int(team_param)
        posts = posts.filter(team_id=selected_team_id)

    teams = Team.objects.order_by("name")

    return render(
        request,
        "forum/forum_list.html",
        {
            "posts": posts,
            "teams": teams,
            "q": q,
            "selected_team_id": selected_team_id,
        },
    )


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully.")
            return redirect("forum:post_detail", pk=post.pk)
        messages.error(request, "Submission failed. Please fix the errors below.")
    else:
        form = PostForm()

    return render(request, "forum/create_post.html", {"form": form})


def post_detail(request, pk):
    post = get_object_or_404(Post.objects.select_related("author", "team"), pk=pk)
    return render(request, "forum/post_detail.html", {"post": post})
