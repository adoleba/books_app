from django import forms


from books_app.books.models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        exclude = []

