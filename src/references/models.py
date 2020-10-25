from django.db import models

# Create your models here.


class Author(models.Model):
    author = models.CharField(
        'Author',
        max_length=50
    )
    description = models.TextField(
        'About Author',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.author


class Genre(models.Model):
    genres = models.CharField(
        'Genre',
        max_length=40,
    )
    description = models.TextField(
        'About Genre',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Language(models.Model):
    languages = models.CharField(
        'Language',
        max_length=40,
    )

    def __str__(self):
        return self.languages


# class Condition(models.Model):
#     conditions = models.CharField(
#         'Condition',
#         max_length=30,
#     )
#
#     def __str__(self):
#         return self.conditions


class BookSeries(models.Model):
    series = models.CharField(
        'Title of the Series',
        max_length=30,
    )
    description = models.TextField(
        'About this Series',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.series


class PublishingHouse(models.Model):
    pubhouse = models.CharField(
        "Publishing House",
        max_length=40,
    )

    otherbooks = models.TextField(
        "Other books of this house",
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.pubhouse
