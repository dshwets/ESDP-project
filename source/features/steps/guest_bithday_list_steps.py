import datetime

from behave import *
from django.urls import reverse

from hostelguests.factories import GuestFactory
from hostelguests.models import Guest


@then('Opens Guest birthday list page')
def step_impl(context):
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    guest_birthday = GuestFactory(birth_date=datetime.date.today())
    guest_no_birthday = GuestFactory(birth_date=yesterday)
    guest_birth_url = reverse('hostelguests:guest_birthday_list')
    context.behave_driver.get(context.get_url(guest_birth_url))


@step('Displays guest birthday list page with "guest"')
def step_impl(context):
    guest = Guest.objects.get(birth_date=datetime.date.today())
    element = context.behave_driver.find_element_by_xpath("//div[1]/h3/b")
    title = "Список именинников"
    guest_element = context.behave_driver.find_element_by_class_name("card-title")
    assert guest_element.text == f'ФИО: {guest.first_name} {guest.last_name}'
    assert element.text == title
