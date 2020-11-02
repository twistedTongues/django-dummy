from django import forms
from . import models


# class CreateCityForm(forms.Form):
#     name = forms.CharField(maxlength=50, required=True)
#
#
# class UpdateCityForm(forms.Form):
#     name = forms.CharField(maxlength=50, required=True)
#     pk = forms.CharField(widget=forms.HiddenInput)
#

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'


class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"
