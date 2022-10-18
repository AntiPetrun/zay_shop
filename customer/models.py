from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    first_name = models.CharField(
        max_length=16
    )
    last_name = models.CharField(
        max_length=32
    )
    phone = models.IntegerField(
        max_length=10,
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
        max_length=200,
        validators=[
            EmailValidator(),
        ]
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'customer_customers'
        verbose_name = 'email'
        verbose_name_plural = 'emails'
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
