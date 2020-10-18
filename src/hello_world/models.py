from django.db import models

# Create your models here.


class Persone(models.Model):
    name = models.CharField(
        "ФИО",
        max_length=70


    )
    phones = models.ManyToManyField(
        'hello_world.Phone',
        verbose_name="Телефоны"
    )

    def __str__(self):
        return self.name


class PhoneType(models.Model):
    phone_type = models.CharField(
        'Тип телефонного номера',
        max_length=5
    )
    description = models.TextField(
        'Описание',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.phone_type + " " + str(self.pk)


class Phone(models.Model):
    number = models.CharField(
        'Номер телефона',
        max_length=20,
        blank=False,
        null=False
    )
    phone_type = models.ForeignKey(
        PhoneType,
        verbose_name="Тип телефона",
        on_delete=models.PROTECT
    )

    # Persone

    def __str__(self):
        return f'{self.number} {self.phone_type.phone_type}'
