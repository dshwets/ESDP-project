from behave import then
from django.urls import reverse

from productincomes.factories import ProductIncomesFactory


@then('Opens Product Income list page')
def step_impl(context):
    product_income = ProductIncomesFactory()
    product_income_url = reverse('product_incom:list_product_incom')
    context.behave_driver.get(context.get_url(product_income_url))


@then('Displays Product Income list page with "{title}" and "{text_name}"')
def step_impl(context, title, text_name):
    element = context.behave_driver.find_element_by_xpath("//div[1]/h3/b")
    title = "Приход товара"
    product_income_element = context.behave_driver.find_element_by_id("id_product_incoms_name")
    text_name = product_income_element.text
    assert element.text == title
    assert text_name is not None