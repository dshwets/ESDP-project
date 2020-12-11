from behave import then
from django.urls import reverse
from journalservices.factories import JournalServiceFactory


@then('I open journalservice view page')
def step_impl(context):
    journalservice = JournalServiceFactory()
    context.journalservice = journalservice
    entry_url = reverse('journalservices:journal_detail', kwargs={'pk': journalservice.pk})
    context.browser.get(context.get_url(entry_url))

@then('It displays "{title}"')
def step_impl(context, title):
    element = context.browser.find_element_by_id('journalservice-title')
    title = "Запись об услуге"
    assert element.text == title
