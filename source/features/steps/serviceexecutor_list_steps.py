from behave import *
from django.urls import reverse
from serviceexecutors.factories import ServiceExecutorFactory


@then('Opens service executor list page')
def step_impl(context):
    serviceexecutor = ServiceExecutorFactory()
    serviceexecutor_url = reverse('serviceexecutors:serviceexecutors_list')
    context.service_executor = serviceexecutor
    context.browser.get(context.get_url(serviceexecutor_url))


@step('Displays serviceexecutor list page with "{title}"')
def step_impl(context, title):
    element = context.browser.find_element_by_xpath("//div[1]/h3/b")
    title = "Список исполнителей услуг"
    service_executor = context.service_executor
    assert element.text == title
    assert service_executor.name == service_executor.name


