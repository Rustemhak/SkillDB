from django.shortcuts import render

from pages.models import SportSkills


def login_0(request):
    return render(request, "login_0.html", {})


def login_1(request):
    return render(request, "login_1.html", {})


def profile(request):
    sskills = SportSkills.objects.all();
    context = {
        'sskills': sskills,
    }
    return render(request, "profile.html", context)


def post(self, request):
    query = request.POST["s1"]
    skill = SportSkills(name=query)
    skill.save()
    context = {
        'skill': skill
    }
    if skill.name == 'бадминтон':
        context = {
            'бадминтон': skill
        }
    return render(request, 'profile.html', context)


def dev(request):
    return render(request, "dev.html", {})
