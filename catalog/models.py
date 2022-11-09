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
        blank=True,
        null=True,
        default=None,
        related_name='subcategories'
    )
    image = models.ImageField(
        upload_to='categories',
        blank=True,
        null=True,
    )
    is_published = models.BooleanField(
        default=False
    )
    slug = models.SlugField(
        unique=True
    )

    def get_absolute_url(self):
        return reverse(
            'catalog:cat_prods',
            kwargs={'cat_slug': self.slug}
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
        related_name='products'
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
        null=True,
        default=None
    )
    brand = models.ForeignKey(
        'cookbook.Brand',
        on_delete=models.PROTECT,
        related_name='products'
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    colors = models.ManyToManyField(
        'cookbook.Color',
        related_name="products"
    )
    specification = models.CharField(
        max_length=255
    )
    sizes = models.ManyToManyField(
        'cookbook.Size',
        related_name="products",
    )
    GENDERS = (
        ('1', 'Man'),
        ('2', 'Woman'),
        ('3', 'Unisex'),
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDERS,
        blank=True,
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

    def display_colors(self):
        return ', '.join([color.name for color in self.colors.all()])

    display_colors.short_description = 'Colors'

    def display_sizes(self):
        return ', '.join([size.name for size in self.sizes.all()])

    display_sizes.short_description = 'Sizes'

    def get_absolute_url(self):
        return reverse(
            'catalog:prod_card',
            kwargs={'prod_slug': self.slug, 'brand': self.brand.id, 'gender': self.gender}
        )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'catalog_products'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('title', 'is_published')
