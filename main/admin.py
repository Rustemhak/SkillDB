from django.contrib import admin

# Register your models here.
from .models import Event


class EventModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "place"]
    list_display_links = ["id"]
    list_editable = ["title"]
    list_filter = ["timestamp"]
    search_fields = ["title", "place"]

    class Meta:
        model = Event


admin.site.register(Event, EventModelAdmin)
