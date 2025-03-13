from django.contrib import admin
from .models import Organizer, Event, Fighter, Fight, Statistics

admin.site.register(Organizer)
admin.site.register(Event)
admin.site.register(Fighter)
admin.site.register(Fight)
admin.site.register(Statistics)
