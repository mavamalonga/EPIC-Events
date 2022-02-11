from django.contrib import admin
<<<<<<< HEAD
from .models import Client, User, Event, Contract

=======
from api.models import User, Client, Event, Contract


>>>>>>> api
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Event)
admin.site.register(Contract)