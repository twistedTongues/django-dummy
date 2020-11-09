from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import (TemplateView, DetailView, ListView, CreateView,
                                  DeleteView, UpdateView)

from .models import Genre, Author, BookSeries, PublishingHouse, Language
from .forms import (CreateGenreForm, CreateAuthorForm, CreateBookSeriesForm,
                    CreatePublishingHouseForm, CreateLanguageForm,
                    UpdateGenreForm, UpdateAuthorForm, UpdateBookSeriesForm,
                    UpdatePublishingHouseForm, UpdateLanguageForm)


class ShowReferencesView(TemplateView):
    template_name = 'references/references_list.html'

    def get_context_data(self, **kwargs):
        author = Author.objects.all()
        genres = Genre.objects.all()
        language = Language.objects.all()
        series = BookSeries.objects.all()
        pubhouse = PublishingHouse.objects.all()
        context = super().get_context_data(**kwargs)
        context['author'] = author
        context['genres'] = genres
        context['language'] = language
        context['series'] = series
        context['publishers'] = pubhouse
        return context


class ShowAuthorListView(ListView):
    model = Author
    template_name = 'references/references_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Authors'
        return context


class ShowGenreListView(ListView):
    model = Genre
    template_name = 'references/references_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Genres'
        return context


class ShowLanguageListView(ListView):
    model = Language
    template_name = 'references/references_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Languages'
        return context


class ShowBookSeriesListView(ListView):
    model = BookSeries
    template_name = 'references/references_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Books of the series'
        return context


class ShowPublishingHouseListView(ListView):
    model = PublishingHouse
    template_name = 'references/references_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Publishing Houses'
        return context


# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     return context


class CreateAuthorView(CreateView):
    # form_class = CreateBookForm
    model = Author
    success_url = "/references"
    template_name = 'references/create_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Author'
        return context


class CreateGenreView(CreateView):
    # form_class = CreateBookForm
    model = Genre
    success_url = "/references"
    template_name = 'references/create_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Genre'
        return context


class CreateLanguageView(CreateView):
    # form_class = CreateBookForm
    model = Language
    success_url = "/references"
    template_name = 'references/create_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Language'
        return context


class CreateBookSeriesView(CreateView):
    # form_class = CreateBookForm
    model = BookSeries
    success_url = "/references"
    template_name = 'references/create_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Serie of the book'
        return context


class CreatePublishingHouseView(CreateView):
    # form_class = CreateBookForm
    model = PublishingHouse
    success_url = "/references"
    template_name = 'references/create_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Publishing House'
        return context


class UpdateAuthorView(UpdateView):
    # form_class = CreateBookForm
    model = Author
    success_url = "/references"
    template_name = 'references/update_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Author'
        return context


class UpdateGenreView(UpdateView):
    # form_class = CreateBookForm
    model = Genre
    success_url = "/references"
    template_name = 'references/update_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Genre'
        return context


class UpdateLanguageView(UpdateView):
    # form_class = CreateBookForm
    model = Language
    success_url = "/references"
    template_name = 'references/update_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Language'
        return context


class UpdateBookSeriesView(UpdateView):
    # form_class = CreateBookForm
    model = BookSeries
    success_url = "/references"
    template_name = 'references/update_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Serie of the book'
        return context


class UpdatePublishingHouseView(UpdateView):
    # form_class = CreateBookForm
    model = PublishingHouse
    success_url = "/references"
    template_name = 'references/update_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Publishing House'
        return context


class DeleteAuthorView(DeleteView):
    template_name = 'references/delete_references.html'
    # form_class = CreateBookForm
    model = Author
    success_url = "/references"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Author'
        return context


class DeleteGenreView(DeleteView):
    template_name = 'references/delete_references.html'
    # form_class = CreateBookForm
    model = Genre
    success_url = "/references"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Genre'
        return context


class DeleteLanguageView(DeleteView):
    template_name = 'references/delete_references.html'
    # form_class = CreateBookForm
    model = Language
    success_url = "/references"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Language'
        return context


class DeleteBookSeriesView(DeleteView):
    template_name = 'references/delete_references.html'
    # form_class = CreateBookForm
    model = BookSeries
    success_url = "/references"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Serie of the book'
        return context


class DeletePublishingHouseView(DeleteView):
    template_name = 'references/delete_references.html'
    # form_class = CreateBookForm
    model = PublishingHouse
    success_url = "/references"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'PublishingHouse'
        return context
# CRUD(L)


def show_references_list_view(request):
    genres = Genre.objects.all()
    author = Author.objects.all()
    languages = Language.objects.all()
    series = BookSeries.objects.all()
    pubhouse = PublishingHouse.objects.all()
    context = {'genres': genres, 'author': author, 'series': series,
               'pubhouse': pubhouse, 'languages': languages}
    return render(request, template_name='references/references_list.html',
                  context=context)


def show_reference_by_pk_view(request, title, ref_id):
    if title == 'genre':
        type = Genre.objects.get(pk=ref_id)
    elif title == 'author':
        type = Author.objects.get(pk=ref_id)
    elif title == 'series':
        type = BookSeries.objects.get(pk=ref_id)
    elif title == 'pubhouse':
        type = PublishingHouse.objects.get(pk=ref_id)
    elif title == 'languages':
        type = Language.objects.get(pk=ref_id)
    context = {'type': type}
    return render(request, template_name='references/reference.html',
                  context=context)


# def create_genres_view(request):
#     if request.method == 'POST':
#         form = CreateGenreForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/references')
#     else:
#         form = CreateGenreForm()
#     return render(request, template_name='references/create_references.html',
#                   context={'form': form, 'header': 'genre'})
#
#
# def create_author_view(request):
#     if request.method == 'POST':
#         form = CreateAuthorForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/references')
#     else:
#         form = CreateAuthorForm()
#     return render(request, template_name='references/create_references.html',
#                   context={'form': form, 'header': 'author'})
#
#
# def create_series_view(request):
#     if request.method == 'POST':
#         form = CreateBookSeriesForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/references')
#     else:
#         form = CreateBookSeriesForm()
#     return render(request, template_name='references/create_references.html',
#                   context={'form': form, 'header': 'series'})
#
#
# def create_pubhouse_view(request):
#     if request.method == 'POST':
#         form = CreatePublishingHouseForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/references')
#     else:
#         form = CreatePublishingHouseForm()
#     return render(request, template_name='references/create_references.html',
#                   context={'form': form, 'header': 'publisher'})
#
#
# def create_languages_view(request):
#     if request.method == 'POST':
#         form = CreateLanguageForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/references')
#     else:
#         form = CreateLanguageForm()
#     return render(request, template_name='references/create_references.html',
#                   context={'form': form, 'header': 'publisher'})
#
#
# def update_genres_view(request, pk):
#     if request.method == 'POST':
#         form = UpdateGenreForm(data=request.POST)
#         if form.is_valid():
#             ref_name = form.cleaned_data.get('genres')
#             ref_description = form.cleaned_data.get('description')
#             obj = Genre.objects.get(pk=pk)
#             obj.genres = ref_name
#             obj.description = ref_description
#             obj.save()
#             return HttpResponseRedirect('/references')
#     else:
#         ref = Genre.objects.get(pk=pk)
#         form = UpdateGenreForm(instance=ref)
#     return render(request, template_name='references/update_references.html',
#                   context={'form': form, 'header': 'genre'})
#
#
# def update_author_view(request, pk):
#     if request.method == 'POST':
#         form = UpdateAuthorForm(data=request.POST)
#         if form.is_valid():
#             ref_name = form.cleaned_data.get('author')
#             ref_description = form.cleaned_data.get('description')
#             obj = Author.objects.get(pk=pk)
#             obj.author = ref_name
#             obj.description = ref_description
#             obj.save()
#             return HttpResponseRedirect('/references')
#     else:
#         ref = Author.objects.get(pk=pk)
#         form = UpdateAuthorForm(instance=ref)
#     return render(request, template_name='references/update_references.html',
#                   context={'form': form, 'header': 'author'})
#
#
# def update_series_view(request, pk):
#     if request.method == 'POST':
#         form = UpdateBookSeriesForm(data=request.POST)
#         if form.is_valid():
#             ref_name = form.cleaned_data.get('series')
#             ref_description = form.cleaned_data.get('description')
#             obj = BookSeries.objects.get(pk=pk)
#             obj.series = ref_name
#             obj.description = ref_description
#             obj.save()
#             return HttpResponseRedirect('/references')
#     else:
#         ref = BookSeries.objects.get(pk=pk)
#         form = UpdateBookSeriesForm(instance=ref)
#     return render(request, template_name='references/update_references.html',
#                   context={'form': form, 'header': 'series'})
#
#
# def update_pubhouse_view(request, pk):
#     if request.method == 'POST':
#         form = UpdatePublishingHouseForm(data=request.POST)
#         if form.is_valid():
#             ref_name = form.cleaned_data.get('pubhouse')
#             obj = PublishingHouse.objects.get(pk=pk)
#             obj.pubhouse = ref_name
#             obj.save()
#             return HttpResponseRedirect('/references')
#     else:
#         ref = PublishingHouse.objects.get(pk=pk)
#         form = UpdatePublishingHouseForm(instance=ref)
#     return render(request, template_name='references/update_references.html',
#                   context={'form': form, 'header': 'publisher'})
#
#
# def update_languages_view(request, pk):
#     if request.method == 'POST':
#         form = UpdateLanguageForm(data=request.POST)
#         if form.is_valid():
#             ref_name = form.cleaned_data.get('languages')
#             obj = Language.objects.get(pk=pk)
#             obj.languages = ref_name
#             obj.save()
#             return HttpResponseRedirect('/references')
#     else:
#         ref = Language.objects.get(pk=pk)
#         form = UpdateLanguageForm(instance=ref)
#     return render(request, template_name='references/update_references.html',
#                   context={'form': form, 'header': 'publisher'})

#
# def delete_genres_view(request, pk):
#     if request.method == 'POST':
#         obj = Genre.objects.get(pk=pk)
#         obj.delete()
#         return HttpResponseRedirect('/references')
#     else:
#         context = {'header': 'genres'}
#     return render(request, template_name='references/delete_references.html',
#                   context=context)
#
#
# def delete_author_view(request, pk):
#     if request.method == 'POST':
#         obj = Author.objects.get(pk=pk)
#         obj.delete()
#         return HttpResponseRedirect('/references')
#     else:
#         context = {'header': 'author'}
#     return render(request, template_name='references/delete_references.html',
#                   context=context)
#
#
# def delete_series_view(request, pk):
#     if request.method == 'POST':
#         obj = BookSeries.objects.get(pk=pk)
#         obj.delete()
#         return HttpResponseRedirect('/references')
#     else:
#         context = {'header': 'series'}
#     return render(request, template_name='references/delete_references.html',
#                   context=context)
#
#
# def delete_pubhouse_view(request, pk):
#     if request.method == 'POST':
#         obj = PublishingHouse.objects.get(pk=pk)
#         obj.delete()
#         return HttpResponseRedirect('/references')
#     else:
#         context = {'header': 'pubhouse'}
#     return render(request, template_name='references/delete_references.html',
#                   context=context)
#
#
# def delete_languages_view(request, pk):
#     if request.method == 'POST':
#         obj = Language.objects.get(pk=pk)
#         obj.delete()
#         return HttpResponseRedirect('/references')
#     else:
#         context = {'header': 'this language'}
#     return render(request, template_name='references/delete_references.html',
#                   context=context)
