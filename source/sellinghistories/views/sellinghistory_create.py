import json

import redis
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from django.conf import settings

from products.models import Product
from sellinghistories.forms import AddProductToCartForm
from sellinghistories.models import SellingHistory


class AddProductToCartView(CreateView):
    template_name = 'sellinghistory_create.html'
    form_class = AddProductToCartForm
    model = SellingHistory
    permission_required = 'sellinghistory.can_add_sellinghistory'

    def get_form_kwargs(self):
        kwargs = super(AddProductToCartView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
        })
        return kwargs

    def get_success_url(self):
        return reverse('sellinghisoty:add_product_in_cart')


class CreateSellingHistory(View):

        def get(self, request, *args, **kwargs):
            red = redis.StrictRedis(connection_pool=settings.REDIS_POOL)
            cart = red.lrange(f'сart:{self.request.user.pk}', 0, -1)
            list_of_products = []
            if cart:
                for cart_entry in cart:
                    cart_entry=json.loads(cart_entry)
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
                SellingHistory.objects.bulk_create(list_of_products)
                red.ltrim(f'сart:{self.request.user.pk}', 0, -1)
                #TODO
                #нужно обновлять каждый товар
            return redirect('sellinghisoty:add_product_in_cart')
