from behave import then

from hostelservices.factories import SellingPriceFactory, PurchasePriceFactory
from hostelservices.models import HostelService


@then('I press update button on the hostelservice')
def step_impl(context):
    hostelservice = HostelService.objects.first()
    sellingprice = SellingPriceFactory(hostel_service=hostelservice)
    purchaseprice = PurchasePriceFactory(hostel_service=hostelservice)
    context.browser.get(context.get_url(f"/hostelservices/{hostelservice.pk}/update/"))


@then('Changes service_name selling_price and purchase_price')
def step_impl(context):
    context.browser.find_element_by_id("id_service_name-service_name").clear()
    context.browser.find_element_by_id("id_service_name-service_name").send_keys("Тестовое имя")
    context.browser.find_element_by_id("id_selling_price-selling_price").clear()
    context.browser.find_element_by_id("id_selling_price-selling_price").send_keys('10000')
    context.browser.find_element_by_id("id_purchase_price-purchase_price").clear()
    context.browser.find_element_by_id("id_purchase_price-purchase_price").send_keys('20000')
