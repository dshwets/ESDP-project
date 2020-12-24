from behave import then
from django.urls import reverse

from sellinghistories.factories import SellingHistoryFactory


@then('Opens Selling History list page')
def step_impl(context):
    sel_his = SellingHistoryFactory()
    sel_his_url = reverse('sellinghistory:list_sellinghistory')
    context.behave_driver.get(context.get_url(sel_his_url))


@then('Displays Selling History list page with "{title}" and "{text_name}"')
def step_impl(context, title, text_name):
    element = context.behave_driver.find_element_by_xpath("//div[1]/h3/b")
    title = "История продаж"
    sel_his_element = context.behave_driver.find_element_by_id("id_sel_his_guest_name")
    text_name = sel_his_element.text
    assert element.text == title
    assert text_name is not None