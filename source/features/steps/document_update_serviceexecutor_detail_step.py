import os
from behave import then, step
from documents.models import Document


@then('I press update button on the document')
def step_impl(context):
    document = Document.objects.first()
    context.behave_driver.get(context.get_url(f"/documents/{document.pk}/update/"))

@then('Changes document title and file')
def step_impl(context):
    title = 'TestTestTiltle'
    context.behave_driver.find_element_by_name('title').send_keys(title)
    elm = context.behave_driver.find_element_by_xpath("//input[@type='file']")
    elm.send_keys(os.path.abspath('hostelguests') + "/static/img/image-not-found.png")

@then('I press confirm save button')
def step_impl(context):
    btn = context.behave_driver.find_element_by_xpath("//input[@value='Сохранить']")
    context.behave_driver.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()
