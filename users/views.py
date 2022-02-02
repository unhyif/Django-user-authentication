from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import *
from .forms import *

def home(request):
    return render(request, "base.html")


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, label_suffix="")
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"{user.name}님의 회원 가입을 축하합니다!" )
            return redirect("users:home")

        messages.error(request, "회원 가입을 다시 시도해 주세요.")
    else:
        form = SignUpForm(label_suffix="")
    return render(request, "users/sign_up.html", {"form":form})


def log_in(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST, label_suffix="")

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"{user.name}님, 환영합니다!")
                return redirect("users:home")

        messages.error(request, "로그인에 실패했습니다.")
    else:
        form = CustomAuthenticationForm(label_suffix="")
    return render(request, "users/log_in.html", {"form":form})


def log_out(request):
    logout(request)
    messages.info(request, "로그아웃 되었습니다.")
    return redirect("users:home")