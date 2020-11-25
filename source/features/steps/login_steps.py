from behave import when, then, given


@given('I open Homepage')
def step_impl(context):
    context.browser.get("http:localhost:8000")


@when('Enter username "{user}" and password "{password}"')
def step_impl(context, user,password):
    context.browser.find_element_by_id("id_username").send_keys(user)
    context.browser.find_element_by_id("id_password").send_keys(password)


@when('Click on login button')
def step_impl(context):
    context.browser.find_element_by_xpath("/html/body/div[1]/form/input[2]").click()


@then('User must have successfully login to the Guest list page with "{text}"')
def step_impl(context, text):
    element = context.browser.find_element_by_xpath("/html/body/div[1]/h3/b")
    text = "Список гостей"
    assert element.text == text

