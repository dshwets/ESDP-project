import json

import redis
from django.contrib.auth import settings

from products.models import Product


class Cart:
    def __init__(self, user_pk):
        self.user_pk = user_pk
        self.red = redis.StrictRedis(connection_pool=settings.REDIS_POOL)
        self.cart_name = f'cart:{self.user_pk}'

    def _get_redis_cart(self):
        self.red.expire(self.cart_name, 3600)
        return self.red.lrange(self.cart_name, 0, -1)

    def add_product(self, cart_entry: dict):
        updated = False
        redis_list = self._get_redis_cart()
        for redis_list_entry in redis_list:
            redis_list_entry_as_dict = json.loads(redis_list_entry)
            if redis_list_entry_as_dict["product_pk"] == cart_entry["product_pk"]:
                redis_list_entry_as_dict['qty'] += cart_entry['qty']
                index = redis_list.index(redis_list_entry)
                redis_list_entry = json.dumps(redis_list_entry_as_dict)
                self.red.lset(self.cart_name, index, redis_list_entry)
                updated = True
        if not updated:
            self.red.lpush(self.cart_name, json.dumps(cart_entry), )

    def get_cart_context_data(self):
        cart = self._get_redis_cart()
        list_of_products = []
        cart_total = 0
        context = {}
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
