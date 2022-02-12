from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import User, Client, Event, Contract


class UserAdmin(UserAdmin):
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff',
                'is_active')

admin.site.register(User, UserAdmin)
admin.site.register(Client)
admin.site.register(Event)
admin.site.register(Contract)