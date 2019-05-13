from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from books_app.books.filters import CategoryFilter
from books_app.books.forms import BookForm


from books_app.books.models import Book, Category, Author


def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()
    book_list = Book.objects.all()
    category_filter = CategoryFilter(request.GET, queryset=book_list)

    return render(request, 'books/templates/books_index.html', {'books': books, 'categories': categories,
                                                                'authors': authors, 'category_filter': category_filter})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            book = Book.objects.create(title=title, description=description)
            book.category.add(*form.cleaned_data['category'])
            book.author.get_or_create(name=form.cleaned_data['author'])
        return redirect('index')

    else:
        form = BookForm(request.POST)

    return render(request, 'books/templates/add_book.html', {'form': form})


def import_book(request):
    return render(request, 'books/templates/import_book.html', )

