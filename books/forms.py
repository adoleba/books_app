from django import forms

from books.models import Author, Category


class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    author = forms.ModelMultipleChoiceField(label='Author(s)', queryset=Author.objects.all().order_by('name'))
    category = forms.ModelMultipleChoiceField(
        label='Category/Categories', queryset=Category.objects.all().order_by('name'))


class AuthorForm(forms.Form):
    name = forms.CharField(label='Firstname, Lastname', max_length=100)


class ImportForm(forms.Form):
    value = forms.CharField(label='Keyword', max_length=100)
