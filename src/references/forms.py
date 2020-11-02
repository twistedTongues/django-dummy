from django import forms

from . import models


class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = ('__all__')


class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ('__all__')


class CreateBookSeriesForm(forms.ModelForm):
    class Meta:
        model = models.BookSeries
        fields = ('__all__')


class CreatePublishingHouseForm(forms.ModelForm):
    class Meta:
        model = models.PublishingHouse
        fields = ('__all__')


class CreateLanguageForm(forms.ModelForm):
    class Meta:
        model = models.Language
        fields = ('__all__')


class UpdateGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = ('__all__')


class UpdateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ('__all__')


class UpdateBookSeriesForm(forms.ModelForm):
    class Meta:
        model = models.BookSeries
        fields = ('__all__')


class UpdatePublishingHouseForm(forms.ModelForm):
    class Meta:
        model = models.PublishingHouse
        fields = ('__all__')


class UpdateLanguageForm(forms.ModelForm):
    class Meta:
        model = models.Language
        fields = ('__all__')
