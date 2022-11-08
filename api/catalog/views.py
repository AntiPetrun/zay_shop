from rest_framework.viewsets import ModelViewSet
from catalog.models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_published=True)
    serializer_class = ProductSerializer
