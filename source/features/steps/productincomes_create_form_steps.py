from behave import then

from products.factories import ProductFactory
from products.models import Product
from serviceexecutors.factories import ServiceExecutorFactory


@then('Opens productincomes create page')
def step_impl(context):
    service_executor = ServiceExecutorFactory()
    context.behave_driver.get(context.get_url(f"/product_incom/create/"))

@then('i input product barcode')
def step_impl(context):
    product = ProductFactory()
    barcode_input=context.behave_driver.find_element_by_id("barcode-find-value")
    barcode_input.clear()
    barcode_input.send_keys(product.barcode)
    btn = context.behave_driver.find_element_by_id("barcode-find")
    context.behave_driver.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()
    barcode_input.clear()
    barcode_input.send_keys("123456789")
    btn.click()


@then('Displays product add form')
def step_impl(context):
    product = Product.objects.first()
    first_element = context.behave_driver.find_element_by_id("product-1-barcode")
    assert first_element.get_attribute('value') == str(product.barcode)
    first_element = context.behave_driver.find_element_by_id("product-1-title")
    assert first_element.get_attribute('value') == str(product.title)
    second_element = context.behave_driver.find_element_by_id("product-2-barcode")
    assert second_element.get_attribute('value') == "123456789"
