from django.shortcuts import render
from django.http import HttpResponse

from books.models import Book


def show_book_list_view(request):
    """Returns list of Book objects"""
    # 1 get objects
    # 2 prepare response
    books = Book.objects.all()
    con = {'book_keys': books}
    return render(request, template_name="books/book_list.html", context=con)


def show_book_by_pk_view(request, book_id):
    book_obj = Book.objects.get(pk=book_id)
    con = {'book': book_obj}
    return render(request, template_name="books/book.html", context=con)
