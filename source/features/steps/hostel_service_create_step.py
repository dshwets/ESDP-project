from behave import then


@then('Opens hostel service create page')
def step_impl(context):
    context.browser.get(context.get_url("/hostelservices/add"))


@then('Changes service_name selling and purchase')
def step_impl(context):
    context.browser.find_element_by_id("id_service_name-service_name").send_keys("Тестовое имя")
    context.browser.find_element_by_id("id_selling_price-selling_price").send_keys('10000')
    context.browser.find_element_by_id("id_purchase_price-purchase_price").send_keys('20000')