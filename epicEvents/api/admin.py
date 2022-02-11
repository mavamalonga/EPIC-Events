from django.contrib import admin
from api.models import User, Client, Event, Contract


admin.site.register(User)
admin.site.register(Client)
admin.site.register(Event)
admin.site.register(Contract)