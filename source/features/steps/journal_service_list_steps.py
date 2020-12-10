from behave import then
from django.urls import reverse
from journalservices.factories import JournalServiceFactory


@then('Opens journal service list page')
def step_impl(context):
    journal = JournalServiceFactory()
    serviceexecutor_url = reverse('journalservices:journal_list')
    context.browser.get(context.get_url(serviceexecutor_url))

@then('Displays journal service list page with "{title}" and "{text_name}"')
def step_impl(context, title, text_name):
    element = context.browser.find_element_by_xpath("//div[1]/h3/b")
    title = "Журнал услуг"
    journal_element = context.browser.find_element_by_id("id_journal_name")
    text_name = journal_element.text
    assert element.text == title
    assert text_name is not None
