from behave import *
from django.urls import reverse

from hostelservices.factories import HostelServiceFactory


@then('Opens hostel service list page')
def step_impl(context):
    hostelservice = HostelServiceFactory()
    hostelservices_url = reverse('hostelservices:hostelservices_list')
    context.browser.get(context.get_url(hostelservices_url))


@step('Displays hostel services list page with "{title}" and "{text_name}"')
def step_impl(context, title, text_name):
    element = context.browser.find_element_by_xpath("//div[1]/h3/b")
    title = "Список услуг"
    hostelsrvice_element = context.browser.find_element_by_xpath("//div[1]/h5")
    text_name = hostelsrvice_element.text
    assert element.text == title
    assert text_name is not None




