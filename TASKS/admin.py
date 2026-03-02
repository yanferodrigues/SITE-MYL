from django.contrib import admin
from tasks.models import Events

class ListEvents(admin.ModelAdmin):
    list_display = ("title", "date")
    list_display_links = ("title", "date")
    search_fields = ("title", "date")
    ordering = ("date", "title")

admin.site.register(Events, ListEvents)
