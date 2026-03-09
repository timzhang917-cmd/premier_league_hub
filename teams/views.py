from django.shortcuts import render


def index(request):
    """Teams 首页"""
    return render(request, 'teams/index.html')
