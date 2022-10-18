from django.db import models
from ..cookbook.models import Color, Brand, Size


class Category(models.Model):
    title = models.CharField(
        max_length=32
    )
    description = models.TextField()
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='subcategories'
    )
    is_published = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'catalog_categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('title',)


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        blank=True,
        limit_choices_to={'is_published': True},
        related_name='categories'
    )
    image = models.ImageField(
        upload_to='products'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='title'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    RATINGS = (
        (None, 'Set you rating'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        blank=True
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.PROTECT,
        related_name="colors"
    )
    specification = models.CharField(
        max_length=255
    )
    size = models.ManyToManyField(
        Size,
        related_name="sizes"
    )
    quantity = models.PositiveSmallIntegerField(
        default=1
    )
    date_created = models.DateField(
        auto_now_add=True,
    )
    date_published = models.DateField(
        auto_now=True
    )
    is_published = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'catalog_products'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('title', 'is_published',)
