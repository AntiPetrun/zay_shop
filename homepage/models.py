from django.db import models
from django.utils.translation import gettext_lazy as _


class Banner(models.Model):
    title = models.CharField(
        max_length=16
    )
    subtitle = models.CharField(
        max_length=24
    )
    body = models.TextField()
    image = models.ImageField(
        upload_to='banners'
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'homepage_banners'
        verbose_name = _('banner')
        verbose_name_plural = _('banners')
        ordering = ('-title',)
