import json

import redis
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from django.conf import settings

from products.models import Product
from sellinghistories.carthelper import Cart
from sellinghistories.forms import AddProductToCartForm
from sellinghistories.models import SellingHistory


class AddProductToCartView(PermissionRequiredMixin, CreateView):
    template_name = 'sellinghistory_create.html'
    form_class = AddProductToCartForm
    model = SellingHistory
    permission_required = 'sellinghistories.can_add_sellinghistory'

    def get_form_kwargs(self):
        kwargs = super(AddProductToCartView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(AddProductToCartView, self).get_context_data(**kwargs)
        cart = Cart(self.request.user.pk)
        context['cart'] = cart.get_cart_context_data()['cart']
        context['cart_total'] = cart.get_cart_context_data()['cart_total']
        return context

    def get_success_url(self):
        return reverse('sellinghistory:add_product_in_cart')


class CreateSellingHistory(PermissionRequiredMixin, View):
    permission_required = 'sellinghistories.can_add_sellinghistory'

    def get(self, request, *args, **kwargs):
        cart = Cart(self.request.user.pk)
        cart.save_to_sellinghistory(self.request)

        return redirect('sellinghistory:add_product_in_cart')
