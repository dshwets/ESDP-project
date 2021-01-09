from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import WatchProduct
from api.serializers import ProductDetailSerializer
from products.models import Product


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
                return Response({"error":"error barcode"}, status=status.HTTP_400_BAD_REQUEST)


class ProductIncomeView(APIView):
    permission_classes = (permission_required("products.can_view_product", raise_exception=True),)
    def post(self, request):
        print(request.data)
        # article = request.data.get('article')
        # # Create an article from the above data
        # serializer = ArticleSerializer(data=article)
        # if serializer.is_valid(raise_exception=True):
        #     article_saved = serializer.save()
        # return Response({"success": "Article '{}' created successfully".format(article_saved.title)})
