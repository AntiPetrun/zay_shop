from django.db import models
from django.contrib.auth import get_user_model

from src.catalog.models import Product

User = get_user_model()


class Comment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        default=None,
        related_name='comments'
    )
    date_created = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'comment_comments'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ('date_created',)
