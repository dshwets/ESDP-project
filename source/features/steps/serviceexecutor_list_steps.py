from behave import *
from django.urls import reverse
from serviceexecutors.factories import ServiceExecutorFactory


@then('Opens service executor list page')
def step_impl(context):
    serviceexecutor = ServiceExecutorFactory()
    serviceexecutor_url = reverse('serviceexecutors:serviceexecutors_list')
    context.browser.get(context.get_url(serviceexecutor_url))


@step('Displays serviceexecutor list page with "{title}" and "{text_name}')
def step_impl(context, title, text_name):
    element = context.browser.find_element_by_xpath("//div[1]/h3/b")
    title = "Список поставщиков услуг"
    serviceexecuter_element = context.browser.find_element_by_xpath("/html/body/div[1]/h3/b")
    text_name = serviceexecuter_element.text
    assert element.text == title
    assert text_name is not None




