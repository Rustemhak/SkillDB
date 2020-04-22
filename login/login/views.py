from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from login.models import MyUser


def logout(request):
    logout(request)


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        surveys = MyUser.objects.filter(email=self.request.user).all()

        context = {
            'surveys': surveys,
        }
        return render(request, 'profile/profile.html', context)
