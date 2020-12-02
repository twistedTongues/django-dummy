from django.views.generic import (DetailView, ListView, CreateView,
                                  DeleteView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


from books.models import Book


class ShowBookDetailView(DetailView):
    template_name = 'books/book.html'
    model = Book


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context


class ShowHomePageListView(ListView):
    template_name = 'books/homepage.html'
    model = Book
    paginate_by = 9
    ordering = ['books']


class ShowBookListView(LoginRequiredMixin, ListView):
    template_name = 'books/book_list.html'
    model = Book
    login_url = "/account/login"
    success_url = "/books"
    paginate_by = 10


class CreateBookView(LoginRequiredMixin, CreateView):
    model = Book
    login_url = "/account/login"
    success_url = "/books"
    template_name = 'books/create_book.html'
    fields = '__all__'


class UpdateBookView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Book
    login_url = "/account/login"
    success_url = "/books"
    template_name = 'books/update_book.html'
    fields = '__all__'


class DeleteBookView(LoginRequiredMixin, DeleteView):
    template_name = 'books/delete_book.html'
    model = Book
    login_url = "/account/login"
    success_url = "/books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
