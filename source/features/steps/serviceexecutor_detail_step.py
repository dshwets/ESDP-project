from behave import then, step
from django.urls import reverse

from serviceexecutors.models import ServiceExecutor


@then('Opens service executor view page')
def step_impl(context):
    serviceexecutor = ServiceExecutor.objects.create(name="John", last_name="Doe", middle_name="Will")
    serviceexecutor_url = reverse('serviceexecutors:serviceexecutor_view', kwargs={'pk': serviceexecutor.pk})
    context.browser.get(context.get_url(serviceexecutor_url))


@then('Displays serviceexecutor "{name}')
def step_impl(context,name):
    element = context.browser.find_element_by_xpath("*//div[1]/h5")
    name = "John Doe Will"
    print("Name dhjjhk:" + name)
    assert element.text == name
