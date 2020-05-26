from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.shortcuts import render
from students.models import Students
from django.views.generic import ListView


class Search(ListView):
    model = Students
    template_name = 'students/search_system.html'

    def get(self, request, *args, **kwargs):

        query = request.GET.get('q')

        if query:
            search = Students.objects.annotate(full_name=Concat('name', Value(' '), 'surname')). \
                filter(Q(full_name__icontains=query) | Q(area=query)).order_by('-id')
        else:
            search = Students.objects.all().order_by('-id')

        context = {
            'messages': 'Не найдено',
            'search_obj': search,
        }
        return render(request, template_name=self.template_name, context=context)
