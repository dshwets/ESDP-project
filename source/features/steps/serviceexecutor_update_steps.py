from behave import when, then, given, step

from serviceexecutors.models import ServiceExecutor


@then('Открыть страницу редактирования исполнителья услуг')
def step_impl(context):
    executor = ServiceExecutor.objects.first()
    context.browser.get(context.get_url(f"/serviceexecutors/{executor.pk}/update/"))


@then('И ввести имя "{name}" фамилия "{last_name}" и отчество "{middle_name}"')
def step_impl(context, name, last_name, middle_name):
    context.browser.find_element_by_id("id_name").send_keys(name)
    context.browser.find_element_by_id("id_last_name").send_keys(last_name)
    context.browser.find_element_by_id("id_middle_name").send_keys(middle_name)


@then('И нажимаю на кнопку сохранить')
def step_impl(context):
    btn = context.browser.find_element_by_xpath("//input[@value='Сохранить']")
    context.browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()

