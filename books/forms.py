from django import forms

from books.models import Author, Category


class BookForm(forms.Form):
    title = forms.CharField(label='Tytuł', max_length=100)
    description = forms.CharField(label='Opis', widget=forms.Textarea)
    author = forms.ModelMultipleChoiceField(label='Autor/Autorzy', queryset=Author.objects.all().order_by('name'))
    category = forms.ModelMultipleChoiceField(
        label='Kategoria/Kategorie', queryset=Category.objects.all().order_by('name'))


class AuthorForm(forms.Form):
    name = forms.CharField(label='Imię i nazwisko', max_length=100)


class ImportForm(forms.Form):
    value = forms.CharField(label='Słowo kluczowe', max_length=100)
