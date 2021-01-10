from behave import then
from django.urls import reverse


@then('I open  employee create page')
def step_impl1(context):
    employee_url = reverse('employees:employee_create')
    context.behave_driver.get(context.get_url(employee_url))


@then('I enter title "first_name"')
def step_impl(context):
    context.behave_driver.find_element_by_id("id_first_name").send_keys("Тестовое имя")
    context.behave_driver.find_element_by_id("id_last_name").send_keys("last_name")
    context.behave_driver.find_element_by_id("id_passport_id").send_keys("11222111")
    context.behave_driver.find_element_by_id("id_phone_number").send_keys("+996500500500")
    context.behave_driver.find_element_by_id("id_relative_phone_number").send_keys("+996500500501")
    context.behave_driver.find_element_by_id("id_address").send_keys("Тестовое имя")
    context.behave_driver.find_element_by_id("id_note").send_keys("Тестовое имя")



