import os

from behave import then



@then('I click on login Добавить Документ')
def step_impl(context):
    context.browser.find_element_by_id("id_add_document").click()

@then('And Changes document title and file')
def step_impl(context):
    title = 'TestTestTiltle'
    elm = context.browser.find_element_by_xpath("//input[@type='file']")
    elm.send_keys(os.path.abspath('hostelguests') + "/static/img/image-not-found.png")


@then('I press confirm add button')
def step_impl(context):
    btn = context.browser.find_element_by_xpath("//input[@value='Сохранить']")
    btn.click()