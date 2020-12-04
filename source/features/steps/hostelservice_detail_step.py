import time

from behave import then
from django.urls import reverse
from hostelservices.factories import HostelServiceFactory
from hostelservices.models import HostelService


@then('Opens hostel service view page')
def step_impl(context):
    service = HostelService.objects.create(service_name="Услуга")
    print(service)
    service_url = reverse('hostelservices:hostelservices_detail', kwargs={'pk': service.pk})
    print(service_url)
    context.browser.get(context.get_url(service_url))

@then('Displays hostel service "{title}')
def step_impl(context,title):
    element = context.browser.find_element_by_id(id="service_name")
    title = "Услуга"
    print("Name dhjjhk:" + title)
    assert element.text == title