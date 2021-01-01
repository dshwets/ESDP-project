from behave import then

from features.steps.beahve_helpers import check_element_not_exists


@then('I open Sellinghistory delete page')
def step_impl(context):
    context.behave_driver.find_element_by_xpath('//table/tbody/tr/td[6]/a').click()


@then('Displays empty Selling History list page')
def step_impl(context):
    assert context.behave_driver.find_element_by_xpath('//table') is not None
    check_element_not_exists(context, '//tabke/tbody')
