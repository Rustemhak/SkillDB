from django.urls import path
from . import views

urlpatterns = [
     path("",views.login_0, name="login_0"),
     path("login",views.login_1, name="login_1"),
     path("profile",views.profile,name="profile"),
     path("profile2",views.profile2,name="profile2"),
]