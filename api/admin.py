from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import User, Client, Event, Contract


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'is_staff', 'is_active')
    list_filter = ('date_joined', 'groups')
    search_fields = ('username', )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'company_name', 'sales_contact_id')
    list_filter = ('date_created', 'date_updated')
    search_fields = ('last_name', )

    def has_add_permission(self, request):
        return super(ClientAdmin, self).has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if obj.sales_contact_id.id == request.user.id:
                return obj.sales_contact_id.id == request.user.id
            return request.user.groups.filter(name='team-gestion').exists()
        return super(ClientAdmin, self).has_change_permission(request, obj=obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            if obj.sales_contact_id.id == request.user.id:
                return obj.sales_contact_id.id == request.user.id
            return request.user.groups.filter(name='team-gestion').exists()
        return super(ClientAdmin, self).has_change_permission(request, obj=obj)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'client_id', 'date', 'support_contact_id')
    list_filter = ('date', )
    search_fields = ('name', )

    def has_add_permission(self, request):
        return super(EventAdmin, self).has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if obj.support_contact_id.id == request.user.id:
                return obj.support_contact_id.id == request.user.id
            return request.user.groups.filter(name='team-gestion').exists()
        return super(EventAdmin, self).has_change_permission(request, obj=obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            if obj.support_contact_id.id == request.user.id:
                return obj.support_contact_id.id == request.user.id
            return request.user.groups.filter(name='team-gestion').exists()
        return super(EventAdmin, self).has_change_permission(request, obj=obj)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'sales_contact_id', 'payment_status')
    list_filter = ('payment_status', )
    search_fields = ('event_id', )

    def has_add_permission(self, request):
        return super(ContractAdmin, self).has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if obj.sales_contact_id.id == request.user.id:
                return obj.sales_contact_id.id == request.user.id
            return request.user.groups.filter(name='team-gestion').exists()
        return super(ContractAdmin,
                     self).has_change_permission(request, obj=obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            if obj.sales_contact_id.id == request.user.id:
                return obj.sales_contact_id.id == request.user.id
            return request.user.groups.filter(name='team-gestion').exists()
        return super(ContractAdmin,
                     self).has_change_permission(request, obj=obj)
