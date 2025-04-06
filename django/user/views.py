from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponse(f"<h1>Welcome, {request.user.username}!</h1>")

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/user/")
    else:
        form = SignupForm()
    return render(request, "users/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/user/")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")
