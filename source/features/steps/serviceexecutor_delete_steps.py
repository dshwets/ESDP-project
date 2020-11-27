from behave import then, step
from serviceexecutors.factories import ServiceExecutorFactory
import time


@step('There is a service executor')
def step_impl(context):
    serviceexecutor = ServiceExecutorFactory(name='Test')
    context.serviceexecutor_pk = serviceexecutor.pk


@then('Open service executor detail page')
def step_impl(context):
    context.browser.get(context.get_url('/serviceexecutors/{}/'.format(context.serviceexecutor_pk)))


@then('I press delete button')
def step_impl(context):
    time.sleep(1)
    context.browser.find_element_by_id("delete-button").click()


@then('I press confirm delete button')
def step_impl(context):
    time.sleep(1)
    context.browser.find_element_by_xpath("//input[@value='Да' and @type='submit']").click()


@then('Then I get to Homepage')
def step_impl(context):
    assert context.browser.current_url == (context.get_url('/') or context.get_url(''))
