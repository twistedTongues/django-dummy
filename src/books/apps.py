from django.apps import AppConfig

from django.db.models.signals import post_delete

# from books.models import Book
# from books.signals import signals


class BooksConfig(AppConfig):
    name = 'books'

    def ready(self):
        from . import signals
        from . import models
        post_delete.connect(signals.photo_cover_cleaner, sender=models.Book)
