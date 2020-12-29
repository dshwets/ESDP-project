from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import permission_required
from api.serializers import ProductDetailSerializer
from products.models import Product


class ProductDetailView(APIView):
    permission_classes = (permission_required("products.can_view_product", raise_exception=True),)

    def get(self, request, barcode):
        product = Product.objects.filter(barcode=barcode, deleted=False)
        if product:
            serializer = ProductDetailSerializer(product[0])
            return Response(serializer.data)
        else:
            return Response({'id': '',
                             'title': '',
                             'barcode': barcode,
                             'purchase_price': ''})