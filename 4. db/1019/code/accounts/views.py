# 장고
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
# 만든 거
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':    # 사용자가 값을 입력했을 때
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:   # GET, 즉 url로 접속했을 때
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()  # 유저 가져오기
            auth_login(request, user)
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('todos:index')