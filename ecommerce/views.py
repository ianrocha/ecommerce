from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def home_page(request):
    context ={
        "title": "Hello World!",
        "content": "Welcome to the homepage",
        "premium_content": "YEAHHH"
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context ={
        "title": "About Page",
        "content": "Welcome to the about page",

    }
    return render(request, "about_page.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in: ")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/login")
        else:
            print("Error")
    return render(request, "auth/login.html", context)


def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})

