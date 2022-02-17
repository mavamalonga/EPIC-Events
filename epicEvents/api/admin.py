from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from api.models import User, Client, Event, Contract
from api.serializers import ClientSerializer, EventSerializer, ContractSerializer
from django.shortcuts import get_object_or_404


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
	list_filter = ('date_joined', )
	search_fields = ('username', )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'id', 'email', 'company_name', 'sales_contact_id')
	list_filter = ('date_created', 'date_updated')
	search_fields = ('last_name', )

	def has_change_permission(self, request, obj=None):
		try:
			pk = request.headers['Referer'].split('/')[6]
			client = get_object_or_404(Client.objects.get(pk=int(pk)))
			return client.sales_contact_id.id == request.user.id
		except Exception as e:
			return True


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'id', 'client_id', 'date', 'support_contact_id')
	list_filter = ('date', )
	search_fields = ('name', )


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
	list_display = ('event_id', 'id', 'client_id', 'sales_contact_id', 'payment_status')
	list_filter = ('payment_status', )
	search_fields = ('event_id', )

