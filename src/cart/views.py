from django.views.generic import TemplateView, DeleteView, RedirectView
from books import models as books
from django.http import Http404
from django.urls import reverse_lazy
from cart import models
from order import models as order_models
# Create your views here.


def create_cart(user, session):
    cart = models.Cart.objects.create(customer=user)
    session['cart_id'] = cart.pk
    return cart


class CartView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        user = self.request.user
        if not user.is_authenticated:
            user = None
        if cart_id:
            cart = models.Cart.objects.filter(pk=cart_id).first()
            if not cart:
                cart = create_cart(user, self.request.session)
        else:
            cart = create_cart(user, self.request.session)
        context['cart'] = cart
        book_id = self.request.GET.get('book')
        if not book_id:
            return context
        try:
            book_id = int(book_id)
        except:
            pass
        book = books.Book.objects.filter(pk=book_id).first()
        if book:
            book_in_cart, created = models.BookInCart.objects.get_or_create(
                book=book,
                cart=cart,
                defaults={
                    'quantity': 1,
                    'price': book.price
                }
            )
            if not created:
                book_in_cart.quantity += 1
                book_in_cart.price = book_in_cart.sum_price()
                book_in_cart.save()
        else:
            pass
        context['book'] = book
        return context


class DeleteBookInCartView(DeleteView):
    model = models.BookInCart
    template_name = 'cart/delete_book_in_cart.html'
    success_url = reverse_lazy('cart:cart')


class UpdateCartView(RedirectView):

    def get_redirect_url(self):
        cart_id = self.request.session.get('cart_id')
        user = self.request.user
        if cart_id:
            cart = models.Cart.objects.filter(pk=cart_id).first()
        else:
            raise Http404(" ")
        btn = self.request.POST.get('submit_button')
        if btn == 'edit':
            obj_list = []
            for book_in_cart_id, quantity in self.request.POST.items():
                if book_in_cart_id not in ['csrfmiddlewaretoken', 'submit_button']:
                    book_in_cart = models.BookInCart.objects.get(pk=int(book_in_cart_id))
                    if book_in_cart.cart.pk == cart_id:
                        book_in_cart.quantity = int(quantity)
                        book_in_cart.price = book_in_cart.sum_price()
                        book_in_cart.save()
                        obj_list.append(book_in_cart)
                    else:
                        raise Http404(" ")
            models.BookInCart.objects.bulk_update(obj_list, ['quantity'])
        else:
            if cart.books.all().count() <= 0:
                return reverse_lazy('cart:cart')
            cart_id = self.request.session.get('cart_id')
            cart = models.Cart.objects.filter(pk=cart_id).first()
            order, created = order_models.Order.objects.get_or_create(
                cart=cart,
                defaults={
                    'cart': cart
                }
            )
            return reverse_lazy('order:update_order')
        return reverse_lazy('cart:cart')
