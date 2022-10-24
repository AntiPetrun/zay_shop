import uuid

from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(
        max_length=32
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        default=None,
        related_name='subcategories'
    )
    is_published = models.BooleanField(
        default=False
    )
    slug = models.SlugField(
        unique=True
    )

    def get_absolute_url(self):
        return reverse(
            'catalog:category_detail',
            kwargs={'category_slug': self.slug}
        )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'catalog_categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('title', 'is_published')


class Product(models.Model):
    article = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
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
        max_digits=6,
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
        blank=True,
        default=None
    )
    brand = models.ForeignKey(
        'cookbook.Brand',
        on_delete=models.PROTECT,
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    color = models.ManyToManyField(
        'cookbook.Color',
        related_name="colors"
    )
    specification = models.CharField(
        max_length=255
    )
    size = models.ManyToManyField(
        'cookbook.Size',
        related_name="sizes"
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
    slug = models.SlugField(
        unique=True
    )

    def display_color(self):
        return ', '.join([color.name for color in self.color.all()])

    display_color.short_description = 'Color'

    def display_size(self):
        return ', '.join([size.name for size in self.size.all()])

    display_size.short_description = 'Size'

    def get_absolute_url(self):
        return reverse(
            'catalog:product_detail',
            kwargs={'prod_slug': self.slug}
        )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'catalog_products'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('title', 'is_published')
