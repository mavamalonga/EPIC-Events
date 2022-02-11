from django.contrib import admin
from .models import Client, User, Event, Contract

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Event)
admin.site.register(Contract)