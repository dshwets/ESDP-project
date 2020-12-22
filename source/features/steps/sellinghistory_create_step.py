from behave import then
from django.urls import reverse
from products.factories import ProductFactory


@then('I Open sell items page')
def step_impl(context):
    sell_items_url = reverse('sellinghisoty:add_product_in_cart')
    context.behave_driver.get(context.get_url(sell_items_url))


@then('I enter product "{barcode}" and  qty "{qty}"')
def step_impl(context, barcode, qty):
    barcode=123456
    qty=10
    ProductFactory(barcode = 123456, qty=100)
    context.behave_driver.find_element_by_id("id_barcode").send_keys("123456")
    context.behave_driver.find_element_by_id("id_qty").send_keys("10")

@then('I pess purchase goods button')
def step_impl(context):
    purchase_cart_url = reverse('sellinghisoty:create_sellinghistory')
    context.behave_driver.get(context.get_url(purchase_cart_url))
