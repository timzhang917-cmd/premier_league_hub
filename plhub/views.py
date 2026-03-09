"""
首页与认证相关视图
"""
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
    """首页：显示欢迎语"""
    return render(request, 'home.html')


def register(request):
    """用户注册（无密码格式与长度限制）"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
