from behave import then
from django.urls import reverse
from products.factories import ProductFactory


@then('I Open sell items page')
def step_impl(context):
    sell_items_url = reverse('sellinghistory:add_product_in_cart')
    context.behave_driver.get(context.get_url(sell_items_url))


@then('I enter product "{barcode}" and  qty "{qty}"')
def step_impl(context, barcode, qty):
    ProductFactory(title='asddsa',barcode=barcode, qty=qty)

    def find_context_and_send_keys(id_element, value):
        context.behave_driver.find_element_by_id(id_element).send_keys(value)

    find_context_and_send_keys("id_barcode", barcode)
    find_context_and_send_keys("id_qty", qty)


@then('I pess purchase goods button')
def step_impl(context):
    purchase_cart_url = reverse('sellinghistory:create_sellinghistory')
    context.behave_driver.get(context.get_url(purchase_cart_url))
