from selenium.webdriver.support.select import Select
from behave import then
from django.urls import reverse

from sellinghistories.factories import SellingHistoryFactory


@then('Opens Selling history update page')
def step_impl(context):
    sel_his = SellingHistoryFactory()
    entry_url = reverse('sellinghistory:sellinghistory_update', kwargs={'pk': sel_his.pk})
    context.behave_driver.get(context.get_url(entry_url))

@then('editing data Selling history')
def step_impl(context):
    context.behave_driver.find_element_by_id("id_qty").clear()
    context.behave_driver.find_element_by_id("id_qty").send_keys("10")