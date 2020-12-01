from behave import then
import time

@then('I press delete button on the document')
def step_impl(context):
    time.sleep(5)
    btn = context.browser.find_element_by_xpath("//input[@value='Удалить документ']")
    btn.click()

#
# @then('Then I get to serviceexecutor page')
# def step_impl(context):
#     assert context.browser.current_url == (context.get_url('serviceexecutors:serviceexecutors_list'))