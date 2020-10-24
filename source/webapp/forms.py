from django import forms
from webapp.models import Photo


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'signature']

