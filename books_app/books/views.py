from django.http import HttpResponse
from django.shortcuts import render

from books_app.books.models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'books/templates/books_index.html', {'books': books})


def add_book(request):
    pass


def import_book(request):
    pass
