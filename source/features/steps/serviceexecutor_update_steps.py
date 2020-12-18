from behave import when, then, given, step

from serviceexecutors.models import ServiceExecutor


@then('Открыть страницу редактирования исполнителья услуг')
def step_impl(context):
    executor = ServiceExecutor.objects.first()
    context.behave_driver.get(context.get_url(f"/serviceexecutors/{executor.pk}/update/"))


@then('И ввести имя "{name}" фамилия "{last_name}" и отчество "{middle_name}"')
def step_impl(context, name, last_name, middle_name):
    context.behave_driver.find_element_by_id("id_name").send_keys(name)
    context.behave_driver.find_element_by_id("id_last_name").send_keys(last_name)
    context.behave_driver.find_element_by_id("id_middle_name").send_keys(middle_name)


@then('И нажимаю на кнопку сохранить')
def step_impl(context):
    btn = context.behave_driver.find_element_by_xpath("//input[@value='Сохранить']")
    context.behave_driver.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()

