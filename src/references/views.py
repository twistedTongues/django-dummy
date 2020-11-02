from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Genre, Author, BookSeries, PublishingHouse, Language
from .forms import (CreateGenreForm, CreateAuthorForm, CreateBookSeriesForm,
                    CreatePublishingHouseForm, CreateLanguageForm,
                    UpdateGenreForm, UpdateAuthorForm, UpdateBookSeriesForm,
                    UpdatePublishingHouseForm, UpdateLanguageForm)


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
    return render(request, template_name='references/references.html',
                  context=context)


def create_genres_view(request):
    if request.method == 'POST':
        form = CreateGenreForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = CreateGenreForm()
    return render(request, template_name='references/create_references.html',
                  context={'form': form, 'header': 'genre'})


def create_author_view(request):
    if request.method == 'POST':
        form = CreateAuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = CreateAuthorForm()
    return render(request, template_name='references/create_references.html',
                  context={'form': form, 'header': 'author'})


def create_series_view(request):
    if request.method == 'POST':
        form = CreateBookSeriesForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = CreateBookSeriesForm()
    return render(request, template_name='references/create_references.html',
                  context={'form': form, 'header': 'series'})


def create_pubhouse_view(request):
    if request.method == 'POST':
        form = CreatePublishingHouseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = CreatePublishingHouseForm()
    return render(request, template_name='references/create_references.html',
                  context={'form': form, 'header': 'publisher'})


def create_languages_view(request):
    if request.method == 'POST':
        form = CreateLanguageForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = CreateLanguageForm()
    return render(request, template_name='references/create_references.html',
                  context={'form': form, 'header': 'publisher'})


def update_genres_view(request, pk):
    if request.method == 'POST':
        form = UpdateGenreForm(data=request.POST)
        if form.is_valid():
            ref_name = form.cleaned_data.get('genres')
            ref_description = form.cleaned_data.get('description')
            obj = Genre.objects.get(pk=pk)
            obj.genres = ref_name
            obj.description = ref_description
            obj.save()
            return HttpResponseRedirect('/references')
    else:
        ref = Genre.objects.get(pk=pk)
        form = UpdateGenreForm(instance=ref)
    return render(request, template_name='references/update_references.html',
                  context={'form': form, 'header': 'genre'})


def update_author_view(request, pk):
    if request.method == 'POST':
        form = UpdateAuthorForm(data=request.POST)
        if form.is_valid():
            ref_name = form.cleaned_data.get('author')
            ref_description = form.cleaned_data.get('description')
            obj = Author.objects.get(pk=pk)
            obj.author = ref_name
            obj.description = ref_description
            obj.save()
            return HttpResponseRedirect('/references')
    else:
        ref = Author.objects.get(pk=pk)
        form = UpdateAuthorForm(instance=ref)
    return render(request, template_name='references/update_references.html',
                  context={'form': form, 'header': 'author'})


def update_series_view(request, pk):
    if request.method == 'POST':
        form = UpdateBookSeriesForm(data=request.POST)
        if form.is_valid():
            ref_name = form.cleaned_data.get('series')
            ref_description = form.cleaned_data.get('description')
            obj = BookSeries.objects.get(pk=pk)
            obj.series = ref_name
            obj.description = ref_description
            obj.save()
            return HttpResponseRedirect('/references')
    else:
        ref = BookSeries.objects.get(pk=pk)
        form = UpdateBookSeriesForm(instance=ref)
    return render(request, template_name='references/update_references.html',
                  context={'form': form, 'header': 'series'})


def update_pubhouse_view(request, pk):
    if request.method == 'POST':
        form = UpdatePublishingHouseForm(data=request.POST)
        if form.is_valid():
            ref_name = form.cleaned_data.get('pubhouse')
            obj = PublishingHouse.objects.get(pk=pk)
            obj.pubhouse = ref_name
            obj.save()
            return HttpResponseRedirect('/references')
    else:
        ref = PublishingHouse.objects.get(pk=pk)
        form = UpdatePublishingHouseForm(instance=ref)
    return render(request, template_name='references/update_references.html',
                  context={'form': form, 'header': 'publisher'})


def update_languages_view(request, pk):
    if request.method == 'POST':
        form = UpdateLanguageForm(data=request.POST)
        if form.is_valid():
            ref_name = form.cleaned_data.get('languages')
            obj = Language.objects.get(pk=pk)
            obj.languages = ref_name
            obj.save()
            return HttpResponseRedirect('/references')
    else:
        ref = Language.objects.get(pk=pk)
        form = UpdateLanguageForm(instance=ref)
    return render(request, template_name='references/update_references.html',
                  context={'form': form, 'header': 'publisher'})


def delete_genres_view(request, pk):
    if request.method == 'POST':
        obj = Genre.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'genres'}
    return render(request, template_name='references/delete_references.html',
                  context=context)


def delete_author_view(request, pk):
    if request.method == 'POST':
        obj = Author.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'author'}
    return render(request, template_name='references/delete_references.html',
                  context=context)


def delete_series_view(request, pk):
    if request.method == 'POST':
        obj = BookSeries.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'series'}
    return render(request, template_name='references/delete_references.html',
                  context=context)


def delete_pubhouse_view(request, pk):
    if request.method == 'POST':
        obj = PublishingHouse.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'pubhouse'}
    return render(request, template_name='references/delete_references.html',
                  context=context)


def delete_languages_view(request, pk):
    if request.method == 'POST':
        obj = Language.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'this language'}
    return render(request, template_name='references/delete_references.html',
                  context=context)
