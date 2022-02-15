from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import User, Client, Event, Contract


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
		if request.user.groups.filter(name='team-support').exists() == True:
			my_clients = []
			for event in Event.objects.filter(support_contact_id=request.user.id):
				my_clients.append(event.client_id.id)
			return Client.objects.filter(pk__in=my_clients)
		elif request.user.groups.filter(name='team-vente').exists() == True:
			my_clients = []
			for client in Client.objects.filter(sales_contact_id=request.user.id):
				my_clients.append(client.id)
			return Client.objects.filter(pk__in=my_clients)
		else:
			return queryset


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'id', 'client_id', 'date', 'support_contact_id')
	#inlines = (ContractInline, )
	list_filter = ('support_contact_id', 'date')
	search_fields = ('name', )

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
	list_display = ('event_id', 'id', 'client_id', 'sales_contact_id', 'payment_status')
