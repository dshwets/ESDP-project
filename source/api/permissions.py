from rest_framework import permissions
from rest_framework import exceptions


def permission_required(permission_name, raise_exception=False):
    class PermissionRequired(permissions.BasePermission):
        def has_permission(self, request, view):
            if not request.user.has_perm(permission_name):
                if raise_exception:
                    raise exceptions.PermissionDenied("Don't have permission")
                return False
            return True
    return PermissionRequired