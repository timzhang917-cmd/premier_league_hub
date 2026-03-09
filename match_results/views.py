from django.shortcuts import render


def index(request):
    """Match Results 首页"""
    return render(request, 'match_results/index.html')
