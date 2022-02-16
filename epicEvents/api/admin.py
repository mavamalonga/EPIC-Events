from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import User, Client, Event, Contract
from api.serializers import ClientSerializer, EventSerializer, ContractSerializer


class ContractInline(admin.TabularInline):
	model = Contract
	extra = 0
	('event_id', 'client_id', 'sales_contact_id')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'id', 'email', 'first_name', 'last_name', 'is_staff',
				'is_active')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'id', 'email', 'company_name', 'sales_contact_id')

	def get_queryset(self, request):
		queryset = super().get_queryset(request)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'id', 'client_id', 'date', 'support_contact_id')
	list_filter = ('date', )
	search_fields = ('name', )

	def get_queryset(self, request):
		queryset = super().get_queryset(request)
		return queryset


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
	list_display = ('event_id', 'id', 'client_id', 'sales_contact_id', 'payment_status')

	def get_queryset(self, request):
		queryset = super().get_queryset(request)
		return queryset