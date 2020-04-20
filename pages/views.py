from django.shortcuts import render


def login_0(request):
    return render(request, "login_0.html", {})


def login_1(request):
    return render(request, "login_1.html", {})


def profile(request):
    return render(request, "profile.html", {})


def profile2(request):
    return render(request, "profile2.html", {})
