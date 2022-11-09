import uuid
from rest_framework.serializers import ModelSerializer
from catalog.models import Product
from slugify import slugify


class ProductSerializer(ModelSerializer):
    def create(self, validated_data):
        validated_data.update(
            {
                'article': uuid.uuid4(),
                'slug': slugify(validated_data.get('title') + validated_data.get('category'))
            }
        )
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, validated_data):
        validated_data.update(
            {
                'slug': slugify(validated_data.get('title') + validated_data.get('category'))
            }
        )
        product = Product(**validated_data)
        product.save()
        return product

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
            'slug',
        )
