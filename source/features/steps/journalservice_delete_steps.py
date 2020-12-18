from behave import then


@then('Displays empty journal service list page with title "{title}"')
def step_impl(context, title):
    assert context.behave_driver.find_element_by_xpath(f'//b[text()="{title}"]') != None
