from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Customer(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    first_name = models.CharField(
        max_length=16
    )
    last_name = models.CharField(
        max_length=32
    )
    phone = models.IntegerField(
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{12}$',
                message='Length has to be 13',
                code='Invalid number'
            )
        ]
    )
    email = models.EmailField(
        max_length=150,
        help_text=_('Enter email in format example@gmail.com'),
        validators=[
            RegexValidator(
                regex="^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$",
                message=_('Invalid email'),
                code=_('invalid_email')
            ),
        ], error_messages={
            "unique": _("Please, enter correct email!.")
        }
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'customer_customers'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
        ordering = ('last_name', 'first_name')


class AddressInfo(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    contact_name = models.CharField(
        max_length=64,
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=32
    )
    street = models.CharField(
        max_length=64
    )
    building = models.CharField(
        max_length=8
    )
    room = models.CharField(
        max_length=8
    )

    def __str__(self):
        return f'{self.city}, {self.street}, {self.building} {self.room}'

    class Meta:
        db_table = 'customer_addresses'
        verbose_name = 'address'
        verbose_name_plural = 'addresses'
        ordering = ('city',)


class Feedback(models.Model):
    name = models.CharField(
        max_length=64
    )
    email = models.EmailField(
        max_length=150,
        help_text=_('Enter email in format example@gmail.com'),
        validators=[
            RegexValidator(
                regex="^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$",
                message=_('Invalid email'),
                code=_('invalid_email')
            ),
        ], error_messages={
            "unique": _("Please, enter correct email!.")
        }
    )
    subject = models.CharField(
        max_length=64
    )
    message = models.TextField()
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'customer_feedbacks'
        verbose_name = _('feedback')
        verbose_name_plural = _('feedbacks')
        ordering = ('date_created',)

