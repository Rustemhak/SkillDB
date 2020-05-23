from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from main.models import Event


def main(request):
    eventList = Event.objects.filter(visible='1')
    paginator = Paginator(eventList, 4)
    page = request.GET.get('page')
    querysetGoods = paginator.get_page(page)

    context = {
        "eventList": eventList,
        "title": "Главная страница блога",
        "desc": "Описание для главной страницы",
        "key": "ключевые, слова",
    }
    return render(request, 'main/main.html', context)


def single(request, id=None):
    post = get_object_or_404(Event, id=id)

    context = {
        "post": post,
    }

    return render(request, 'main/event_info.html', context)
