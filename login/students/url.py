from django.conf.urls import url

from students.views import Search

urlpatterns = [
    # url(r'^search_students/', StudentView.as_view(), name='search_students'),
    url(r'^search/', Search.as_view(), name='search'),
]