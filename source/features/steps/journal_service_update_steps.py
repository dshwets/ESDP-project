from selenium.webdriver.support.select import Select
from behave import then
from django.urls import reverse

from hostelservices.factories import HostelServiceFactory, PurchasePriceFactory, SellingPriceFactory
from journalservices.factories import JournalServiceFactory
from serviceexecutors.factories import ServiceExecutorFactory



@then('Opens journal service update page')
def step_impl(context):
    journal = JournalServiceFactory()
    context.journalservice = journal
    entry_url = reverse('journalservices:journal_update', kwargs={'pk': journal.pk})
    context.browser.get(context.get_url(entry_url))

@then('editing data')
def step_impl(context):
    h_service = HostelServiceFactory()
    select_fr = Select(context.browser.find_element_by_id("id_hostel_service"))
    select_fr.select_by_index(2)
    select_2 = Select(context.browser.find_element_by_id("id_service_executor"))
    select_2.select_by_index(1)
    select_3 = Select(context.browser.find_element_by_id("id_purchase_price"))
    select_3.select_by_index(0)
    select_4 = Select(context.browser.find_element_by_id("id_selling_price"))
    select_4.select_by_index(0)

