from django.shortcuts import render
from django.views.generic import (DetailView, ListView, CreateView,
                                  DeleteView, UpdateView, DetailView)

from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book
# from .forms import CreateBookForm, UpdateBookForm


# wrong but still working way


# def show_book_list_view(request):
#     """Returns list of Book objects"""
#     # 1 get objects
#     # 2 prepare response
#     books = Book.objects.all()
#     con = {'book_keys': books}
#     return render(request, template_name="books/book_list.html", context=con)


# def show_book_by_pk_view(request, book_id):
#     book_obj = Book.objects.get(pk=book_id)
#     con = {'book': book_obj}
#     return render(request, template_name="books/book.html", context=con)
#

# def static_view(request):
#     return render(request, template_name="books/static.html", context={})


# class StaticView(TemplateView):
#     template_name = "books/static.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["vasia"] = "Vasily"
#         return context

class ShowBookDetailView(DetailView):
    template_name = 'books/book.html'
    model = Book


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context


class ShowBookListView(ListView):
    # template_name = 'books/book_list.html'
    model = Book

    # def def_queryset(self):
    #     return super().get_queryset()[0:2]


class CreateBookView(CreateView):
    # form_class = CreateBookForm
    model = Book
    success_url = "/books"
    template_name = 'books/create_book.html'
    fields = '__all__'


class UpdateBookView(UpdateView):
    # form_class = CreateBookForm
    model = Book
    success_url = "/books"
    template_name = 'books/update_book.html'
    fields = '__all__'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["rate"] = 1.488
    #     return context


class DeleteBookView(DeleteView):
    template_name = 'books/delete_book.html'
    # form_class = CreateBookForm
    model = Book
    success_url = "/books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# CRUD(L)
# C, U


# def create_city_view(request):
#     if request.method == "POST":
#         form = CreateCityForm(data=request.POST)
#         if form.is_valid():
#             city_name = form.cleaned_data.get('name')
#             City.objects.create(name=city_name)
#             return HttpResponseRedirect("/")
#     else:
#         form = CreateCityForm()
#     return render(
#         request,
#         template_name="books/create_city.html",
#         context={"form": form})
#
#
# def update_city_view(request, pk):
#     if request.method == "POST":
#         form = UpdateCityForm(data=request.POST)
#         if form.is_valid():
#             city_name = form.cleaned_data.get('name')
#             form_pk = form.clean.get('pk')
#             obj = City.objects.get(pk=form_pk).name = city_name
#             obj.name = city_name
#             obj.save()
#             return HttpResponseRedirect("/")
#     else:
#         city = City.objects.get(pk=pk)
#         form = CreateCityForm(data={'name': city.name, "pk": city.pk})
#     return render(
#         request,
#         template_name="books/create_city.html",
#         context={"form": form})
#
#

# def create_book_view(request):
#     if request.method == "POST":
#         form = CreateBookForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/")
#     else:
#         form = CreateBookForm()
#     return render(
#         request,
#         template_name="books/create_book.html",
#         context={"form": form})
#
#
# def delete_book_view(request, pk):
#     if request.method == "POST":
#         book = Book.objects.get(pk=pk)
#         book.delete()
#         return HttpResponseRedirect("/")
#     else:
#         book = Book.objects.get(pk=pk)
#     return render(
#         request,
#         template_name="books/delete_book.html",
#         context={"book": book})
#
#
# def update_book_view(request, pk):
#     if request.method == "POST":
#         form = UpdateBookForm(request.POST, request.FILES)
#         if form.is_valid():
#             get_name = form.cleaned_data.get('books')
#             get_description = form.cleaned_data.get('description')
#             get_price = form.cleaned_data.get('price')
#             get_author = form.cleaned_data.get('author')
#             get_series = form.cleaned_data.get('series')
#             get_genres = form.cleaned_data.get('genres')
#             get_date_of_establishment = form.cleaned_data.get(
#                 'date_of_establishment')
#             get_amount_of_pages = form.cleaned_data.get('amount_of_pages')
#             get_binding = form.cleaned_data.get('binding')
#             get_format = form.cleaned_data.get('format')
#             get_isbn_id = form.cleaned_data.get('isbn_id')
#             get_book_weight = form.cleaned_data.get('book_weight')
#             get_age_limit = form.cleaned_data.get('age_limit')
#             get_pub_house = form.cleaned_data.get('pub_house')
#             get_conditions = form.cleaned_data.get('conditions')
#             get_number_of_books = form.cleaned_data.get('number_of_books')
#             get_book_availability = form.cleaned_data.get('book_availability')
#             get_rating = form.cleaned_data.get('rating')
#             get_languages = form.cleaned_data.get('languages')
#             obj = Book.objects.get(pk=pk)
#             obj.books = get_name
#             obj.description = get_description
#             obj.price = get_price
#             obj.author.set(get_author)
#             obj.series = get_series
#             obj.genres.set(get_genres)
#             obj.date_of_establishment = get_date_of_establishment
#             obj.amount_of_pages = get_amount_of_pages
#             obj.binding = get_binding
#             obj.format = get_format
#             obj.isbn_id = get_isbn_id
#             obj.book_weight = get_book_weight
#             obj.age_limit = get_age_limit
#             obj.pub_house = get_pub_house
#             obj.conditions = get_conditions
#             obj.number_of_books = get_number_of_books
#             obj.book_availability = get_book_availability
#             obj.rating = get_rating
#             obj.languages.set(get_languages)
#             obj.save()
#             return HttpResponseRedirect("/")
#     else:
#         book = Book.objects.get(pk=pk)
#         form = UpdateBookForm(instance=book)
#     return render(
#         request,
#         template_name="books/update_book.html",
#         context={"form": form})
