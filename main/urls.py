from django.conf.urls import url
from django.urls import path, include
from django.views.generic import DetailView

from . import views
from .models import Event

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Event, template_name="main/event_info.html")),
    url(r'^join', views.join, name='join'),
]
