from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='profile'
    )
    group = models.CharField(
        'Group',
        max_length=20,
        default='User',
        blank=True,
        null=True
    )
    profile_image = models.ImageField(
        verbose_name='Profile image',
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        'Phone number',
        max_length=35,
        default=""
    )
    country = models.CharField(
        'Country',
        max_length=50,
        default=""
    )
    city = models.CharField(
        'City',
        max_length=50,
        default=""
    )
    state = models.CharField(
        'State',
        max_length=50,
        blank=True,
        null=True
    )
    address = models.CharField(
        'First address',
        max_length=50,
        default=""
    )
    index = models.CharField(
        'Index',
        max_length=15,
        default=""
    )

    def __str__(self):
        return f'Profile {self.pk}.'

    class Meta:
        verbose_name = 'Profile'


class CreditCart(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
        related_name='credit_cards'
    )
    card_number = models.IntegerField(
        'Card Number',
        blank=True,
        null=True
    )
    card_date = models.CharField(
        'Card date',
        max_length=5,
        blank=True,
        null=True
    )
    name = models.CharField(
        verbose_name='Name on the back',
        max_length=30,
        blank=True,
        null=True
    )
    cvv = models.PositiveIntegerField(
        verbose_name='CVV',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"""Bank card {self.pk}, user's{self.profile}."""

    class Meta:
        verbose_name = 'Bank Card'
