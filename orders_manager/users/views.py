from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users.forms import LoginUserForm


def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cl_data = form.cleaned_data
            user = authenticate(
                request, username=cl_data["username"], password=cl_data["password"]
            )
            if user and user.is_active:
                login(request, user)
                return redirect("profile_page")
    else:
        form = LoginUserForm()

    return render(request, "users/login.html", {"form": form})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("users/login.html")
    else:
        return redirect("index.html")


def profile_user(request):
    return render(request, "users/profile.html")
