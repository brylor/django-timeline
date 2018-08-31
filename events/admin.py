from django.contrib import admin

from .models import Event, EventAdmin

admin.site.register(Event, EventAdmin)
