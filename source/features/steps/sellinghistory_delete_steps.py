from behave import then
from selenium.common.exceptions import NoSuchElementException

@then('I open Sellinghistory delete page')
def step_impl(context):
    context.behave_driver.find_element_by_xpath('//table/tbody/tr/td[6]/a').click()


@then('Displays empty Selling History list page')
def step_impl(context):
    assert context.behave_driver.find_element_by_xpath('//table') is not None
    try:
        context.behave_driver.find_element_by_xpath('//table/tbody')
        raise Exception('Element was founded')
    except NoSuchElementException:
        pass
