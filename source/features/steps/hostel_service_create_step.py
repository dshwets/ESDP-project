import time

from behave import then
from django.urls import reverse

from hostelservices.factories import SellingPriceFactory, PurchasePriceFactory
from hostelservices.models import HostelService


@then('Opens hostel service create page')
def step_impl(context):

    context.browser.get(context.get_url("/hostelservices/add"))


@then('Changes service_name selling_price and purchase_price')
def step_impl(context):
    time.sleep(3)
    context.browser.find_element_by_id("id_service_name-service_name").send_keys("Тестовое имя")
    context.browser.find_element_by_id("id_selling_price-selling_price").send_keys('10000')
    context.browser.find_element_by_id("id_purchase_price-purchase_price").send_keys('20000')
    #context.browser.find_element_by_xpath("//input[@value='Сохранить']").click()