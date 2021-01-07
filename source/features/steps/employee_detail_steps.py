from behave import then
from django.urls import reverse

from employees.factories import EmployeeFactory


@then('I open  employee detail page')
def step_impl1(context):
    employee = EmployeeFactory()
    employee_url = reverse('employees:employee_detail', kwargs={'pk': employee.pk})
    context.behave_driver.get(context.get_url(employee_url))


@then('Displays employee with "{employee_name}"')
def step_impl(context, employee_name):
    element = context.behave_driver.find_element_by_id("employee_name")
    page_title = context.behave_driver.find_element_by_id("employee_title")
    employee_name = element.text
    assert employee_name is not None
    assert page_title.text == "Информация о сотруднике"