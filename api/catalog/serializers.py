from rest_framework.serializers import ModelSerializer
from catalog.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'article',
            'category',
            'image',
            'title',
            'price',
            'rating',
            'brand',
            'description',
            'colors',
            'specification',
            'sizes',
            'gender',
            'is_published',
        )
