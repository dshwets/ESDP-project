from behave import then
from django.urls import reverse
from hostelservices.factories import HostelServiceFactory, PurchasePriceFactory, SellingPriceFactory



@then('Opens hostel service view page')
def step_impl(context):
    service = HostelServiceFactory()
    purchase_price = PurchasePriceFactory(
        hostel_service=service,
        purchase_price = '50'
    )
    selling_price = SellingPriceFactory(
        hostel_service=service,
        selling_price = '50'
    )
    service_url = reverse('hostelservices:hostelservices_detail', kwargs={'pk': service.pk})
    context.purchase_price = purchase_price
    context.selling_price = selling_price
    context.browser.get(context.get_url(service_url))

@then('Displays hostel service "{name}"')
def step_impl(context, name):
    element = context.browser.find_element_by_xpath("//div[1]/h3/b")
    title = "Услуга"
    hostelsrvice_element = context.browser.find_element_by_xpath("//div[1]/h5")
    text_name = hostelsrvice_element.text
    assert element.text == title
    assert text_name is not None