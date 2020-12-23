import redis

from behave import then
from django.urls import reverse
from django.conf import settings


@then('I pess delete good from cart button')
def step_impl(context):
    cart_name = 'cart:0'
    red = redis.StrictRedis(connection_pool=settings.REDIS_POOL)
    remove_item_from_cart = reverse('sellinghisoty:remove_product_from_cart', kwargs={'pk': 0})
    context.behave_driver.get(context.get_url(remove_item_from_cart))
    assert red.lrange(cart_name, 0, -1) == []
