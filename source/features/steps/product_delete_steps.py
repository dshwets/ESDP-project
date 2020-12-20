from behave import then, step


@then('Displays empty product list page with title "{title}"')
def step_impl(context, title):
    assert context.behave_driver.find_element_by_xpath(f'//b[text()="{title}"]') != None