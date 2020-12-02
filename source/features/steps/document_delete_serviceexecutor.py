from behave import *

@then('I press delete button on the document')
def step_impl(context):
    btn = context.browser.find_element_by_xpath("//input[@value='Удалить документ']")
    context.browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()

@then('And I see that there is no document')
def step_impl(context):
    no_doc = context.browser.find_elements_by_xpath("//*[contains(text(), 'Нет документов')]")[0].text
    assert no_doc == f'Нет документов'