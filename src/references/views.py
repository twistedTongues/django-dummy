from django.contrib.auth.mixins import LoginRequiredMixin

from books.models import Book
from django.views.generic import (TemplateView, DetailView, ListView,
                                  CreateView, DeleteView, UpdateView)

from django.views.generic.list import MultipleObjectMixin
from .models import Genre, Author, BookSeries, PublishingHouse, Language
from .forms import (CreateGenreForm, CreateAuthorForm, CreateBookSeriesForm,
                    CreatePublishingHouseForm, CreateLanguageForm,
                    UpdateGenreForm, UpdateAuthorForm, UpdateBookSeriesForm,
                    UpdatePublishingHouseForm, UpdateLanguageForm)


class ShowReferencesView(LoginRequiredMixin, TemplateView):
    template_name = 'references/all_references.html'
    login_url = "/account/login"
    success_url = "/books"

    def get_context_data(self, **kwargs):
        author = Author.objects.all()
        genres = Genre.objects.all()
        languages = Language.objects.all()
        series = BookSeries.objects.all()
        pubhouse = PublishingHouse.objects.all()
        context = super().get_context_data(**kwargs)
        context['author'] = author
        context['genres'] = genres
        context['languages'] = languages
        context['series'] = series
        context['pubhouse'] = pubhouse
        return context


class ShowAuthorListView(LoginRequiredMixin, ListView):
    model = Author
    template_name = 'references/references_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Authors'
        return context


class ShowGenreListView(LoginRequiredMixin, ListView):
    model = Genre
    template_name = 'references/references_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Genres'
        return context


class ShowLanguageListView(LoginRequiredMixin, ListView):
    model = Language
    template_name = 'references/references_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Languages'
        return context


class ShowBookSeriesListView(LoginRequiredMixin, ListView):
    model = BookSeries
    template_name = 'references/references_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Books of the series'
        return context


class ShowPublishingHouseListView(LoginRequiredMixin, ListView):
    model = PublishingHouse
    template_name = 'references/references_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Publishing Houses'
        return context


class ShowAuthorByPkView(LoginRequiredMixin, DetailView,
                         MultipleObjectMixin):
    model = Author
    paginate_by = 7
    template_name = 'references/references_by_pk.html'

    def get_context_data(self, **kwargs):
        object_list = Book.objects.filter(author=self.get_object())
        context = super(ShowAuthorByPkView, self).get_context_data(
            object_list=object_list, **kwargs)
        context['type'] = 'author'
        return context


class ShowGenreByPkView(LoginRequiredMixin, DetailView,
                        MultipleObjectMixin):
    model = Genre
    paginate_by = 7
    template_name = 'references/references_by_pk.html'

    def get_context_data(self, **kwargs):
        object_list = Book.objects.filter(genres=self.get_object())
        context = super(ShowGenreByPkView, self).get_context_data(
            object_list=object_list, **kwargs)
        context['type'] = 'genres'
        return context


class ShowLanguageByPkView(LoginRequiredMixin, DetailView,
                           MultipleObjectMixin):
    model = Language
    paginate_by = 7
    template_name = 'references/references_by_pk.html'

    def get_context_data(self, **kwargs):
        object_list = Book.objects.filter(languages=self.get_object())
        context = super(ShowLanguageByPkView, self).get_context_data(
            object_list=object_list, **kwargs)
        context['type'] = 'languages'
        return context


class ShowBookSeriesByPkView(LoginRequiredMixin, DetailView,
                             MultipleObjectMixin):
    model = BookSeries
    paginate_by = 7
    template_name = 'references/references_by_pk.html'

    def get_context_data(self, **kwargs):
        object_list = Book.objects.filter(series=self.get_object())
        context = super(ShowBookSeriesByPkView, self).get_context_data(
            object_list=object_list, **kwargs)
        context['type'] = 'series'
        return context


class ShowPublishingHouseByPkView(LoginRequiredMixin, DetailView,
                                  MultipleObjectMixin):
    model = PublishingHouse
    paginate_by = 7
    template_name = 'references/references_by_pk.html'

    def get_context_data(self, **kwargs):
        object_list = Book.objects.filter(pubhouse=self.get_object())
        context = super(ShowPublishingHouseByPkView, self).get_context_data(
            object_list=object_list, **kwargs)
        context['type'] = 'pubhouse'
        return context


class CreateAuthorView(LoginRequiredMixin, CreateView):
    model = Author
    success_url = "/references"
    template_name = 'references/create_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Author'
        return context


class CreateGenreView(LoginRequiredMixin, CreateView):
    model = Genre
    success_url = "/references"
    template_name = 'references/create_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Genre'
        return context


class CreateLanguageView(LoginRequiredMixin, CreateView):
    model = Language
    success_url = "/references"
    template_name = 'references/create_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Language'
        return context


class CreateBookSeriesView(LoginRequiredMixin, CreateView):
    model = BookSeries
    success_url = "/references"
    template_name = 'references/create_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Serie of the book'
        return context


class CreatePublishingHouseView(LoginRequiredMixin, CreateView):
    model = PublishingHouse
    success_url = "/references"
    template_name = 'references/create_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Publishing House'
        return context


class UpdateAuthorView(LoginRequiredMixin, UpdateView):
    model = Author
    success_url = "/references"
    template_name = 'references/update_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Author'
        return context


class UpdateGenreView(LoginRequiredMixin, UpdateView):
    model = Genre
    success_url = "/references"
    template_name = 'references/update_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Genre'
        return context


class UpdateLanguageView(LoginRequiredMixin, UpdateView):
    model = Language
    success_url = "/references"
    template_name = 'references/update_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Language'
        return context


class UpdateBookSeriesView(LoginRequiredMixin, UpdateView):
    model = BookSeries
    success_url = "/references"
    template_name = 'references/update_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Serie of the book'
        return context


class UpdatePublishingHouseView(LoginRequiredMixin, UpdateView):
    model = PublishingHouse
    success_url = "/references"
    template_name = 'references/update_references.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Publishing House'
        return context


class DeleteAuthorView(LoginRequiredMixin, DeleteView):
    template_name = 'references/delete_references.html'
    model = Author
    success_url = "/references"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Author'
        return context


class DeleteGenreView(LoginRequiredMixin, DeleteView):
    template_name = 'references/delete_references.html'
    model = Genre
    success_url = "/references"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Genre'
        return context


class DeleteLanguageView(LoginRequiredMixin, DeleteView):
    template_name = 'references/delete_references.html'
    model = Language
    success_url = "/references"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Language'
        return context


class DeleteBookSeriesView(LoginRequiredMixin, DeleteView):
    template_name = 'references/delete_references.html'
    model = BookSeries
    success_url = "/references"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Serie of the book'
        return context


class DeletePublishingHouseView(LoginRequiredMixin, DeleteView):
    template_name = 'references/delete_references.html'
    model = PublishingHouse
    success_url = "/references"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'PublishingHouse'
        return context
