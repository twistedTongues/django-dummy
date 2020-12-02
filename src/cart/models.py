from django.db import models
from django.contrib.auth import get_user_model


from books.models import Book


User = get_user_model()


class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        related_name='carts',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        "Created date",
        auto_now=False,
        auto_now_add=True,
    )
    last_updated_date = models.DateTimeField(
        "Last updated date",
        auto_now=True,
        auto_now_add=False,
    )

    def total_price(self):
        price = 0
        for book_in_cart in self.books.all():
            price += book_in_cart.price
        return price

    def total_items(self):
        quantity = 0
        for book_in_cart in self.books.all():
            quantity += book_in_cart.quantity
        return quantity

    def __str__(self):
        return f'Cart {self.pk}, customer: {self.customer}'

    class Meta:
        verbose_name = 'Cart'


class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="books"

    )
    quantity = models.IntegerField(
        "Quantity",
        default=1,
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='books_in_carts'
    )

    price = models.DecimalField(
        "Price",
        decimal_places=2,
        max_digits=10,

    )

    def sum_price(self):
        return self.quantity * self.book.price

    def __str__(self):
        return f'Book(s) in cart{self.pk}, number of books: {self.quantity},\
        price: {self.price}'

    class Meta:
        verbose_name = 'Books in cart'
