from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Comment(models.Model):
    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        related_name='products'
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

    def get_absolute_url(self):
        return reverse(
            'comment:comment_detail',
            kwargs={'comment_pk': self.pk}
        )

    class Meta:
        db_table = 'comment_comments'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ('date_created',)
