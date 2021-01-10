import time

from behave import then
from selenium.webdriver.support.ui import Select

from productincomes.models import Incomes, ProductIncomes
from products.models import Product
from serviceexecutors.models import ServiceExecutor


@then('I fill out the form with data')
def step_impl(context):
    select = Select(context.behave_driver.find_element_by_id("serviceexecutor"))
    select.select_by_index(0)
    title2 = context.behave_driver.find_element_by_id("product-2-title")
    title2.clear()
    title2.send_keys('Test2')
    qty2 = context.behave_driver.find_element_by_id("product-2-qty")
    qty2.clear()
    qty2.send_keys('12')
    price2 = context.behave_driver.find_element_by_id("product-2-purchase-price")
    price2.clear()
    price2.send_keys('20')
    qty1 = context.behave_driver.find_element_by_id("product-1-qty")
    qty1.clear()
    qty1.send_keys('15')
    price1 = context.behave_driver.find_element_by_id("product-1-purchase-price")
    price1.clear()
    price1.send_keys('50')
    submit = context.behave_driver.find_element_by_id("final-form-submit")
    context.behave_driver.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
    time.sleep(3)
    product = Product.objects.filter(barcode=123456789).first()
    assert product.title == 'Test2'
    serviceexecutor = ServiceExecutor.objects.first()
    new_incomes = Incomes.objects.first()
    assert new_incomes.services_executor == serviceexecutor

