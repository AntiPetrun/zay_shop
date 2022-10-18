from django.db import models


class Brand(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='brand'
    )
    image = models.ImageField(
        upload_to='brands'
    )

    def __str__(self):
        return self.name

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
