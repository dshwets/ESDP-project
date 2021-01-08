from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.views.generic.base import View

from sellinghistories.carthelper import Cart


class DeleteProductFromCart(PermissionRequiredMixin, View):
    permission_required = 'sellinghistories.can_add_sellinghistory'

    def get(self, request, *args, **kwargs):
        cart = Cart(self.request.user.pk)
        cart.delete_from_cart(self.kwargs['pk'])

        return redirect('sellinghistory:add_product_in_cart')


