from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView

from product.models import Product
from .serializers import ProductSerializer

class ProductListView(ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer