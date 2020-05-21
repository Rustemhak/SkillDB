from django.contrib import admin

# Register your models here.
from students.models import Students


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'area')
    search_fields = ('name', 'surname', 'area')
    list_filter = ('name', 'surname', 'area')

    class Meta:
        model = Students


admin.site.register(Students, StudentsAdmin)
