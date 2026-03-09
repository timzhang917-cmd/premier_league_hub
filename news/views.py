from django.shortcuts import render


def index(request):
    """News 首页"""
    return render(request, 'news/index.html')
