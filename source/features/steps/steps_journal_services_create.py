from selenium.webdriver.support.select import Select
from behave import then
from hostelguests.factories import GuestFactory
from hostelservices.factories import HostelServiceFactory, PurchasePriceFactory, SellingPriceFactory
from journalservices.factories import JournalServiceFactory
from serviceexecutors.factories import ServiceExecutorFactory


@then('Opens guest detail page')
def step_impl(context):
    journal = JournalServiceFactory(
        guest=GuestFactory(),
        hostel_service=HostelServiceFactory(),
        service_executor=ServiceExecutorFactory(),
        purchase_price=PurchasePriceFactory(),
        selling_price=SellingPriceFactory()
    )
    context.behave_driver.get(context.get_url(f"/guest/{journal.guest.pk}/detail/"))

@then('I click on Добавить услугу button')
def step_impl(context):
    context.behave_driver.find_element_by_name("button-journal-add").click()

@then('Changes hostel service, service executor')
def step_impl(context):
    select_fr = Select( context.behave_driver.find_element_by_id("id_hostel_service"))
    select_fr.select_by_index(0)
    select_2 = Select( context.behave_driver.find_element_by_id("id_service_executor"))
    select_2.select_by_index(0)
    select_3 = Select( context.behave_driver.find_element_by_id("id_service_executor"))
    select_3.select_by_index(0)
    select_4 = Select( context.behave_driver.find_element_by_id("id_service_executor"))
    select_4.select_by_index(0)



