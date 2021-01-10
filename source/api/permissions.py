from rest_framework import permissions


class BasePermissionRequired(permissions.BasePermission):
    def has_permission(self, request, view, permission_name=None):
        if request.user.has_perm(permission_name):
            return True
        else:
            return False


class WatchProduct(BasePermissionRequired):
    def has_permission(self, request, view, permission_name='products.can_view_product'):
        return super(WatchProduct, self).has_permission(request, view, permission_name)


class AddIncomes(BasePermissionRequired):
    def has_permission(self, request, view, permission_name='productincomes.can_add_incomes'):
        return super(AddIncomes, self).has_permission(request, view, permission_name)