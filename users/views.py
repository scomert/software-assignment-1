from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User


# Create your views here.
from django.urls import reverse


def signup(request):
    if request.method == "POST":
        User.objects.create_user(username=request.POST.get("username"),
                                 password=request.POST.get("password"))
        return HttpResponse("Success!")

    return render(request, "register.html")


def login(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect(reverse("entries"))

    return render(request, "registration/login.html", [])
