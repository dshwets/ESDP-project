from behave import then, step
from django.urls import reverse

from serviceexecutors.models import ServiceExecutor


@then('Opens service executor view page')
def step_impl(context):
    serviceexecutor = ServiceExecutor.objects.create(name="John", last_name="Doe", middle_name="Will")
    serviceexecutor_url = reverse('serviceexecutors:serviceexecutor_view', kwargs={'pk': serviceexecutor.pk})
    context.behave_driver.get(context.get_url(serviceexecutor_url))


@then('Displays serviceexecutor "{name}')
def step_impl(context,name):
    element = context.behave_driver.find_element_by_xpath("//h5[@class='card-title']")
    name = "John Doe Will"
    print("Name dhjjhk:" + name)
    assert element.text == name
