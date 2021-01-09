from behave import then
from django.urls import reverse

from employees.factories import EmployeeFactory
from employees.models import Employee


@then('Opens employees list page')
def step_impl(context):
    employee = EmployeeFactory()
    employee_list_url = reverse('employees:employee_list')
    context.behave_driver.get(context.get_url(employee_list_url))

@then('Displays employees list page with "{employee_last_name}')
def step_impl(context, employee_last_name):
    employee = Employee.objects.all().first()
    employee_last_name_element = context.behave_driver.find_element_by_id(employee.last_name)
    assert employee.last_name == employee_last_name_element.text