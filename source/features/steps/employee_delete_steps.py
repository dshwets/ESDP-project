from behave import then, step
from employees.factories import EmployeeFactory


@step('There is an employee')
def step_impl(context):
    employee = EmployeeFactory()
    context.employee_pk = employee.pk


@then('Open employee delete page')
def step_impl(context):
    context.behave_driver.get(context.get_url('/employees/{}/delete/'.format(context.employee_pk)))


@step('I press confirm delete employee button')
def step_impl(context):
    context.behave_driver.find_element_by_id("confirm-delete-btn").click()


@step('Then I get to employees list page')
def step_impl(context):
    assert context.behave_driver.current_url == (context.get_url('employees:employee_list'))
