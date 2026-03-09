from django.shortcuts import render


def index(request):
    """League Table 首页"""
    return render(request, 'league_table/index.html')
