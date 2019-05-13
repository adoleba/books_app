from django.http import HttpResponse
from django.shortcuts import render
from books_app.books.filters import CategoryFilter


from books_app.books.models import Book, Category, Author


def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()
    book_list = Book.objects.all()
    category_filter = CategoryFilter(request.GET, queryset=book_list)

    return render(request, 'books/templates/books_index.html', {'books': books, 'categories': categories,
                                                                'authors': authors, 'category_filter': category_filter})


def category_filter(request):
    book_list = Book.objects.all()
    category_filter = CategoryFilter(request.GET, queryset=book_list)
    return render(request, 'books/templates/books_index.html', {'category_filter': category_filter})


def add_book(request):
    pass


def import_book(request):
    pass



