from behave import then
from django.urls import reverse


@then('Opens create product page')
def step_impl(context):
    product_create_url = reverse('products:product_create')
    context.behave_driver.get(context.get_url(product_create_url))


@then('I enter title "test" and last qty "10"')
def step_impl(context):
    context.behave_driver.find_element_by_id("id_title").send_keys("Тестовое имя")
    context.behave_driver.find_element_by_id("id_qty").send_keys("10")
