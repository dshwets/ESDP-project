from behave import then


@then('Opens create service executor page')
def step_impl(context):
    context.behave_driver.get(context.get_url("/serviceexecutors/add/"))


@then('I enter name "{name}" and last name "{last_name}" and middle name "{middle_name}"')
def step_impl(context, name, last_name, middle_name):
    context.behave_driver.find_element_by_id("id_name").send_keys(name)
    context.behave_driver.find_element_by_id("id_last_name").send_keys(last_name)
    context.behave_driver.find_element_by_id("id_middle_name").send_keys(middle_name)


@then('I press submit button')
def step_impl(context):
    btn = context.behave_driver.find_element_by_xpath("//input[@value='Добавить']")
    context.behave_driver.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()


@then('Opens serviceexecutor detail page with "{text}"')
def step_impl(context, text):
    element = context.behave_driver.find_element_by_xpath("/html/body/div[1]/h3/b")
    text = "Поставщик"
    assert element.text == text
