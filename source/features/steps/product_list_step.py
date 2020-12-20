from behave import then
from django.urls import reverse

from products.factories import ProductFactory
from products.models import Product


@then('Opens hostel product list page')
def step_impl(context):
    product = ProductFactory()
    product_list_url = reverse('products:product_list')
    context.behave_driver.get(context.get_url(product_list_url))


@then('Displays product list page with "{product_title}" and "{qty}"')
def step_impl(context, product_title, qty):
    product = Product.objects.all().first()
    product_title_element = context.behave_driver.find_element_by_id(product.title)
    assert product.title == product_title_element.text
    product_qty_element = context.behave_driver.find_element_by_id(f'{product.title}-{product.qty}')
    assert str(product.qty) == product_qty_element.text