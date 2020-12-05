from behave import then, step
from hostelservices.factories import HostelServiceFactory


@step('There is a hostel service')
def step_impl(context):
    hostelservice = HostelServiceFactory()
    context.hostelservice_pk = hostelservice.pk


@then('Open hostel service delete page')
def step_impl(context):
    context.browser.get(context.get_url('/hostelservices/{}/delete/'.format(context.hostelservice_pk)))


@step('I press confirm delete hostel service button')
def step_impl(context):
    context.browser.find_element_by_id("confirm-delete-btn").click()


@step('Then I get to hostel services list page')
def step_impl(context):
    assert context.browser.current_url == (context.get_url('hostelservices:hostelservices_list'))
