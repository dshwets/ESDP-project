from behave import then


@then('Displays empty journal service list page with title "{title}"')
def step_impl(context, title):
    assert context.browser.find_element_by_xpath(f'//b[text()="{title}"]') != None
