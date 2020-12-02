from django.db import models
from references.models import *
from datetime import date

# Create your models here.


class Book(models.Model):
    books = models.CharField(
        'Title of the Book',
        max_length=1000
    )

    description = models.TextField(
        'About Book',
        blank=True,
        null=True,
        max_length=300,
    )
    photo_cover = models.ImageField(
        "Cover of the book",
        upload_to='',
        blank=True,
        null=True
    )

    price = models.DecimalField(
        "Price in USA dollars",
        default=0,
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False
    )

    author = models.ManyToManyField(
        Author,
        verbose_name="Author",
        related_name="book"
    )

    series = models.ForeignKey(
        BookSeries,
        verbose_name="Title of the Serie",
        default=1,
        related_name="book",
        on_delete=models.PROTECT
    )

    genres = models.ManyToManyField(
        Genre,
        verbose_name="Genre",
        related_name="book"
    )

    date_of_establishment = models.DateTimeField(
        verbose_name="Date of establishment",
        blank=True,
        null=True

    )

    amount_of_pages = models.PositiveIntegerField(
        verbose_name="Amount of Pages",
        default=0,
    )

    binding_choice = (('1', 'Paperback'), ('2', 'Hardcover'),
                      ('3', 'Large Print'),
                      ('4', 'Audible Audiobook'), ('5', 'Printed Access Code'),
                      ('6', 'Loose Leaf'),
                      ('7', 'Audio CD'), ('8', 'Board Book'))

    binding = models.CharField(
        verbose_name="Binding",
        default=1,
        max_length=100,
        choices=binding_choice,
    )

    format_choice = (('1', '70×90/8'), ('2', '70×90/16'), ('3', '70×90/32'),
                     ('4', '70×108/32'), ('5', '60×90/16'), ('6', '60×90/32'),
                     ('7', '84×108/32'))

    format = models.CharField(
        verbose_name="Format",
        default=1,
        max_length=100,
        choices=format_choice,
    )

    isbn_id = models.CharField(
        verbose_name="ISBN",
        default='',
        max_length=20,
    )

    book_weight = models.PositiveIntegerField(
        verbose_name="Book's weight in Weight (g)",
        default=0,
    )

    age_limit_choice = (('1', '3+'), ('2', '6+'), ('3', '12+'), ('4', '14+'),
                        ('5', '16 +'), ('6', '18+'), ('7', '21+'))

    age_limit = models.CharField(
        verbose_name="Age limit",
        default=1,
        max_length=4,
        choices=age_limit_choice,
    )

    pubhouse = models.ForeignKey(
        PublishingHouse,
        default=1,
        related_name="book",
        on_delete=models.PROTECT
    )

    condition_choice = (('1', 'New'), ('2', 'Used'), ('3', 'Collectible'))

    conditions = models.CharField(
        verbose_name="conditions",
        default=1,
        max_length=4,
        choices=condition_choice
    )

    number_of_books = models.PositiveIntegerField(
        verbose_name="Number of Books Available",
        default=0,

    )

    AVAILABLE = [
        ('yes', "AVAILABLE"),
        ('no', 'NOT AVAILABLE')
    ]

    book_availability = models.CharField(
        'Book Status',
        max_length=20,
        default='no',
        choices=AVAILABLE
    )

    rating_choice = (('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'),
                     ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
                     ('8', '8'), ('9', '9'), ('10', '10'))

    rating = models.CharField(
        verbose_name="Rating of the book",
        max_length=5,
        default=0,
        choices=rating_choice,
    )

    book_adding_date = models.DateField(
        verbose_name='Publishing date in shop',
        auto_now=False,
        auto_now_add=True
    )

    book_updating_date = models.DateTimeField(
        verbose_name='Date of updating Book',
        auto_now=True,
        auto_now_add=False
    )

    languages = models.ManyToManyField(
        Language,
        verbose_name="Language",
    )

    def __str__(self):
        return f'{self.books} | Book was added: {self.book_adding_date}'
        # | Last updated: {self.book_updating_date}'


class Meta:
    verbose_name = 'Book'
