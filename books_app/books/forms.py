from django import forms
from django.forms import ModelMultipleChoiceField

from books_app.books.models import Category


class BookForm(forms.Form):
    title = forms.CharField(label='Tytuł', max_length=100)
    description = forms.CharField(label='Opis', widget=forms.Textarea)
    author = forms.CharField(label='Autor', max_length=100)
    category = forms.ModelMultipleChoiceField(label='Kategorie', queryset=Category.objects.all())
