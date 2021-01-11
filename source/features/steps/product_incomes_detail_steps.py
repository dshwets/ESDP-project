from behave import then, step
from django.urls import reverse

from productincomes.factories import IncomesFactory, ProductIncomesFactory
from productincomes.models import Incomes, ProductIncomes
from serviceexecutors.factories import ServiceExecutorFactory
from serviceexecutors.models import ServiceExecutor


@then('Opens product incomes view page')
def step_impl(context):
    # serviceexecutor = ServiceExecutor.objects.create(name="John", last_name="Doe", middle_name="Will")
    serviceexecutor = ServiceExecutorFactory()
    incomes = IncomesFactory(services_executor=serviceexecutor)
    productincomes = ProductIncomesFactory(incomes=incomes)
    incomes_url = reverse('product_incom:product_incom_detail', kwargs={'pk': incomes.pk})
    context.behave_driver.get(context.get_url(incomes_url))


@then('Displays product incomes fields')
def step_impl(context):
    service_executor = ServiceExecutor.objects.all().first()
    incomes = Incomes.objects.all().first()
    productincomes = ProductIncomes.objects.filter(incomes=incomes)
    element_ser_exe = context.behave_driver.find_element_by_id("service-executor")
    assert element_ser_exe.text == f'Поставщик: {service_executor.last_name} {service_executor.name} {service_executor.middle_name}'
    element_product = context.behave_driver.find_element_by_id("product-title")
    assert element_product.text == productincomes[0].product.title
    element_product_barcode = context.behave_driver.find_element_by_id("product-barcode")
    assert int(element_product_barcode.text) == productincomes[0].product.barcode