from behave import then

from products.models import Product


@then('I press update button on the product')
def step_impl(context):
    product = Product.objects.first()
    context.behave_driver.get(context.get_url(f"/product/{product.pk}/update/"))

@then('Changes title and qty product')
def step_impl(context):
    context.behave_driver.find_element_by_id("id_title").clear()
    context.behave_driver.find_element_by_id("id_title").send_keys("Тестовое имя")
    context.behave_driver.find_element_by_id("id_qty").clear()
    context.behave_driver.find_element_by_id("id_qty").send_keys('10000')
    context.behave_driver.find_element_by_id("id_purchase_price").clear()
    context.behave_driver.find_element_by_id("id_purchase_price").send_keys('89.12')