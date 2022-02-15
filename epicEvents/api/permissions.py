from rest_framework.permissions import BasePermission, SAFE_METHODS


class StaffAccessPermission(BasePermission):
    message = 'Permission only to the staff member.'

    def has_permission(self, request, view):
        return request.user.is_staff == True


class UserAccessPermission(BasePermission):
     message = 'Permission only to the team-gestion'

     def has_permission(self, request, view):
        return request.user.groups.filter(name='team-gestion').exists() == True or \
            request.user.is_superuser == True


class ClientAccessPermission(BasePermission):
     message = 'Request not allowed.'

     def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        else:
            return request.user.groups.filter(name='team-vente').exists() == True or \
                request.user.groups.filter(name='team-gestion').exists() == True 


class EventAccessPermission(BasePermission):
    message = 'Permission only to the staff member.'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        return request.user.groups.filter(name='team-support').exists() == True 


class ContractAccessPermission(BasePermission):
    message = 'Request not allowed.'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        else:
            return request.user.groups.filter(name='team-vente').exists() == True or \
                    request.user.groups.filter(name='team-gestion').exists() == True 




