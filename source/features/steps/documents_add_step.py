import os

from behave import then
from django.urls import reverse

from serviceexecutors.factories import ServiceExecutorFactory


@then('Opens documents add page')
def step_impl(context):
    context.browser.get(context.get_url("/serviceexecutors/1/documents_add/"))

@then('And Changes document title and file')
def step_impl(context,):
    title = 'TestTestTiltle'
    print(title)
    context.browser.find_element_by_name('title').send_keys(title)
    elm = context.browser.find_element_by_xpath("//input[@type='file']")
    elm.send_keys(os.path.abspath('hostelguest') + "/static/img/image-not-found.pn")

@then('I press confirm add button')
def step_impl(context):
    btn = context.browser.find_element_by_xpath("//input[@value='Сохранить']")
    btn.click()