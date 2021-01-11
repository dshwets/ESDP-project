from decimal import Decimal

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import WatchProduct, AddIncomes
from api.serializers import ProductDetailSerializer
from productincomes.models import Incomes, ProductIncomes
from products.models import Product
from serviceexecutors.models import ServiceExecutor


class ProductDetailView(APIView):
    permission_classes = [
        WatchProduct,
    ]

    def get(self, request, barcode):
        product = Product.objects.filter(barcode=barcode, deleted=False)
        if product:
            serializer = ProductDetailSerializer(product[0])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                isinstance(barcode, int)
                return Response({'id': '',
                                 'title': '',
                                 'barcode': barcode,
                                 'purchase_price': ''}, status=status.HTTP_200_OK)
            except:
                return Response({"error": "error barcode"}, status=status.HTTP_400_BAD_REQUEST)


class ProductIncomeView(APIView):
    permission_classes = [
        AddIncomes,
    ]

    def post(self, request):
        data = request.data
        if data['serviceexecutor']:
            initials = data['serviceexecutor'].split(' ')
            service_executor = ServiceExecutor.objects.get(last_name=initials[0])
            if int(len(data)) < 2:
                return Response({"error": "Заполните все поля"}, status=status.HTTP_400_BAD_REQUEST)
            incomes = Incomes.objects.create(services_executor=service_executor,
                                             created_by=request.user)
            range_product = int((len(data)-1)/4)
            for i in range(range_product):
                i += 1
                title = data[f'title-{i}']
                barcode = int(data[f'barcode-{i}'])
                qty = int(data[f'qty-{i}'])
                purchase_price = Decimal(data[f'purchase-price-{i}'])

                new_product = Product.objects.filter(barcode=barcode)
                if not new_product:
                    Product.objects.create(title=title,
                                           barcode=barcode)
                else:
                    if new_product[0].title == title and new_product[0].deleted == True:
                        new_product[0].deleted = False
                product = Product.objects.get(barcode=barcode)
                ProductIncomes.objects.create(incomes=incomes,
                                              product=product,
                                              qty=qty)
                product.qty += qty
                product.purchase_price = purchase_price
                product.save()
            return Response({'success': incomes.pk}, status=status.HTTP_200_OK)
        return Response({"error": "Заполните все поля"}, status=status.HTTP_400_BAD_REQUEST)
