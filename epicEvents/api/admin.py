from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import User, Client, Event, Contract


class UserAdmin(UserAdmin):
	list_display = ('username', 'id', 'email', 'first_name', 'last_name', 'is_staff',
                'is_active')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'id', 'email', 'company_name', 'sales_contact_id')

class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'id', 'client_id', 'date', 'support_contact_id')

class ContractAdmin(admin.ModelAdmin):
	list_display = ('event_id', 'id', 'client_id', 'sales_contact_id', 'payment_status')


admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Contract, ContractAdmin)