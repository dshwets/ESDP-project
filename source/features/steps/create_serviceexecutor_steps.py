from behave import when, then, given, step

@then('Opens create service executor page')
def step_impl(context):
    context.browser.get(context.get_url("/serviceexecutors/add/"))


@then('I enter name "{name}" and last name "{last_name}" and middle name "{middle_name}"')
def step_impl(context, name, last_name, middle_name):
    context.browser.find_element_by_id("id_name").send_keys(name)
    context.browser.find_element_by_id("id_last_name").send_keys(last_name)
    context.browser.find_element_by_id("id_middle_name").send_keys(middle_name)


@then('I press submit button')
def step_impl(context):
    context.browser.find_element_by_xpath("//input[@value='Добавить']").click()


@then('Opens main page')
def step_impl(context):
    assert context.browser.current_url == context.get_url('/')
