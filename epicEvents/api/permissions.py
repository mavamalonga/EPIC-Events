from rest_framework import permissions


class StaffAccessPermission(permissions.BasePermission):
    message = 'Only staff acess permission'

    def has_permission(self, request, view):
        return request.user.is_staff == True


class GestionTeamAccessPermission(permissions.BasePermission):
     message = 'Only member gestion-team acess permission'

     def has_permission(self, request, view):
        return request.user.groups.filter(name='team-gestion').exists() == True or \
            request.user.is_superuser == True


class GestionTeamAccessPermission(permissions.BasePermission):
     message = 'Only member gestion-team acess permission'

     def has_permission(self, request, view):
        return request.user.groups.filter(name='team-gestion').exists() == True or \
            request.user.is_superuser == True