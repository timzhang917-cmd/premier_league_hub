from django.shortcuts import render


def index(request):
    """Forum 首页"""
    return render(request, 'forum/index.html')
