import redis
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.views.generic.base import View
from django.conf import settings


class DeletePRoductFromCart(PermissionRequiredMixin, View):
    permission_required = 'sellinghistories.can_delete_sellinghistory'

    def get(self, request, *args, **kwargs):
        red = redis.StrictRedis(connection_pool=settings.REDIS_POOL)
        cart_name = f'cart:{self.request.user.pk}'
        cart = red.lrange(cart_name, 0, -1)
        cart_entry = cart[self.kwargs['pk']]
        red.lrem(cart_name, 0, cart_entry)

        return redirect('sellinghistory:add_product_in_cart')


