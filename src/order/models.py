from django.db import models

# Create your models here.
from cart import models as cart


class Order(models.Model):
    cart = models.OneToOneField(
        cart.Cart,
        related_name='order',
        on_delete=models.PROTECT
    )
    comment = models.TextField(
        'Comment about order',
        blank=True,
        null=True
    )
    type_of_payment = models.CharField(
        'Type of payment',
        default=1,
        max_length=20
    )
    date_add = models.DateTimeField(
        'Adding date',
        auto_now=False,
        auto_now_add=True,
    )
    date_last_change = models.DateTimeField(
        'Last change date',
        auto_now=True,
        auto_now_add=False,
    )

    def __str__(self):
        return f'Order {self.pk}'

    class Meta:
        verbose_name = 'Order'
