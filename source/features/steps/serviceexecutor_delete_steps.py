from behave import then, step
from serviceexecutors.factories import ServiceExecutorFactory
import time


@step('There is a service executor')
def step_impl(context):
    serviceexecutor = ServiceExecutorFactory(name='Test')
    context.serviceexecutor_pk = serviceexecutor.pk


@then('Open service executor detail page')
def step_impl(context):
    context.behave_driver.get(context.get_url('/serviceexecutors/{}/'.format(context.serviceexecutor_pk)))


@then('I press delete button')
def step_impl(context):
    time.sleep(1)
    context.behave_driver.find_element_by_id("delete-button").click()


@then('I press confirm delete button')
def step_impl(context):
    time.sleep(1)
    context.behave_driver.find_element_by_xpath("//input[@value='Да' and @type='submit']").click()


@then('Then I get to serviceexecutor page')
def step_impl(context):
    assert context.behave_driver.current_url == (context.get_url('serviceexecutors:serviceexecutors_list'))
