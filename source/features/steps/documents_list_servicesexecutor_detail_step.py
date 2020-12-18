from behave import then, step
from django.urls import reverse
import time
from documents.factories import DocumentFactory
from serviceexecutors.factories import ServiceExecutorFactory



@then('Opens document in service executor view page')
def step_impl(context):
    serviceexecutor = ServiceExecutorFactory()
    document = DocumentFactory(
        service_executor=serviceexecutor
    )
    serviceexecutor_url = reverse('serviceexecutors:serviceexecutor_view', kwargs={'pk': serviceexecutor.pk})
    context.document = document
    context.behave_driver.get(context.get_url(serviceexecutor_url))


@then('Displays docements "{title}')
def step_impl(context,title):
    document = DocumentFactory()
    title = context.document.title
    assert title == title