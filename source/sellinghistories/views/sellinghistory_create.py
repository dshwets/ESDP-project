import json

import redis
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from django.conf import settings

from products.models import Product
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
        red = redis.StrictRedis(connection_pool=settings.REDIS_POOL)
        cart = red.lrange(f'cart:{self.request.user.pk}', 0, -1)
        list_of_products = []
        cart_total = 0
        if cart:
            for cart_entry in cart:
                cart_entry = json.loads(cart_entry)
                product = Product.objects.get(pk=cart_entry['product_pk'])
                cart_entry['product'] = product
                cart_entry['total_by_item'] = product.selling_price * cart_entry['qty']
                cart_total += cart_entry['total_by_item']
                list_of_products.append(cart_entry)
            context['cart'] = list_of_products
            context['cart_total'] = cart_total
        return context

    def get_success_url(self):
        return reverse('sellinghisoty:add_product_in_cart')


class CreateSellingHistory(PermissionRequiredMixin, View):
    permission_required = 'sellinghistories.can_add_sellinghistory'

    def get(self, request, *args, **kwargs):
        red = redis.StrictRedis(connection_pool=settings.REDIS_POOL)
        cart = red.lrange(f'cart:{self.request.user.pk}', 0, -1)
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
            red.delete(f'cart:{self.request.user.pk}')

        return redirect('sellinghisoty:add_product_in_cart')
