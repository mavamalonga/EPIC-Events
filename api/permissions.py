from rest_framework.permissions import BasePermission, SAFE_METHODS


class StaffAccessPermission(BasePermission):
    message = 'Permission only to the staff member.'

    def has_permission(self, request, view):
        return request.user.is_staff


class UserAccessPermission(BasePermission):
    message = 'Permission only to the gestion contact'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        return request.user.groups.filter(name='team-gestion').exists()


class ClientAccessPermission(BasePermission):
    message = 'Permission only to the sales contact'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        return request.user.groups.filter(name='team-vente').exists()

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        else:
            if obj.sales_contact_id.id == request.user.id:
                return obj.sales_contact_id.id == request.user.id
            return request.user.groups.filter(name='team-gestion').exists()


class EventAccessPermission(BasePermission):
    message = 'Permission only to project managers'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        return request.user.groups.filter(name='team-vente').exists()

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        else:
            if obj.support_contact_id.id == request.user.id:
                return obj.support_contact_id.id == request.user.id
            return request.user.groups.filter(name='team-gestion').exists()


class ContractAccessPermission(BasePermission):
    message = 'Permission only to the sales contact'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        return request.user.groups.filter(name='team-vente').exists()

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        else:
            if obj.sales_contact_id.id == request.user.id:
                return obj.sales_contact_id.id == request.user.id
            return request.user.groups.filter(name='team-gestion').exists()
