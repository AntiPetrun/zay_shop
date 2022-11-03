from django.db import models
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='brand'
    )
    image = models.ImageField(
        upload_to='brands'
    )
    slug = models.SlugField(
        unique=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'cookbook:brand_detail',
            kwargs={'brand_slug': self.slug}
        )

    class Meta:
        db_table = 'cookbook_brands'
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
        ordering = ('name',)


class Color(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='color',
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cookbook_colors'
        verbose_name = 'color'
        verbose_name_plural = 'colors'
        ordering = ('name',)


class Size(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cookbook_sizes'
        verbose_name = 'size'
        verbose_name_plural = 'sizes'
        ordering = ('name',)
