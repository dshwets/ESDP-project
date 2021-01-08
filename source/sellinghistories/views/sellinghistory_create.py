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
        red = redis.StrictRedis(connection_pool=settings.REDIS_POOL)
        cart_name = f'cart:{self.request.user.pk}'
        cart = red.lrange(cart_name, 0, -1)
        list_of_products = []
        current_good_list = []
        if cart:
            for cart_entry in cart:
                cart_entry = json.loads(cart_entry)
                product = Product.objects.get(pk=cart_entry['product_pk'])
                list_of_products.append(
                    SellingHistory(
                        qty=cart_entry['qty'],
                        guest=None,
                        product=product,
                        purchase_price=product.purchase_price,
                        selling_price=product.selling_price,
                        created_by=self.request.user
                    )
                )
                if product not in current_good_list:
                    product.qty -= cart_entry['qty']
                    current_good_list.append(product)
                else:
                    product_index = current_good_list.index(product)
                    product = current_good_list[product_index]
                    product.qty -= cart_entry['qty']
                    current_good_list[product_index] = product
            SellingHistory.objects.bulk_create(list_of_products)
            Product.objects.bulk_update(current_good_list, ['qty'])
            red.delete(cart_name)

        return redirect('sellinghistory:add_product_in_cart')
