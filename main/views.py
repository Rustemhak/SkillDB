from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/main.html')


def main(request):
    return render(request, 'main/event_info.html')