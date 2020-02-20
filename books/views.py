import requests
from django.shortcuts import render, redirect

from books.filters import QuerysetFilter
from books.forms import BookForm, AuthorForm, ImportForm
from books.models import Book, Category, Author


def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()
    book_list = Book.objects.all()
    category_filter = QuerysetFilter(request.GET, queryset=book_list)

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
            book.author.add(*form.cleaned_data['author'])
        return redirect('index')

    else:
        form = BookForm()

    return render(request, 'books/templates/add_book.html', {'form': form})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            authors_in_qs = Author.objects.values()
            list_of_authors = [author['name'] for author in authors_in_qs]
            name = form.cleaned_data['name']
            if name not in list_of_authors:
                author = Author.objects.create(name=name)
        return redirect('add_book')

    else:
        form = AuthorForm()

    return render(request, 'books/templates/add_author.html', {'form': form})


def set_import(request):

    if request.method == "POST":
        form = ImportForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            value_url = 'https://www.googleapis.com/books/v1/volumes?q=' + value
            import_book(request, value_url=value_url)
            return redirect(index)

    else:
        form = ImportForm()

    return render(request, 'books/templates/import_book.html', {'form': form})


def import_book(request, value_url):
    response = requests.get(value_url)
    data = response.json()
    books_data = data['items']
    for value in books_data:
        book_dict = value['volumeInfo']
        title = book_dict['title']

        if 'description' in book_dict:
            description = book_dict['description']
        else:
            description = "No description"

        authors = book_dict['authors']

        if 'categories' in book_dict:
            categories = book_dict['categories']
        else:
            categories = ""

        book = Book.objects.create(title=title, description=description)

        for author in authors:
            authors_in_qs = Author.objects.values()
            list_of_authors = [author['name'] for author in authors_in_qs]
            if author in list_of_authors:
                author_name = Author.objects.get(name=author)
                book.author.add(author_name)
            else:
                book.author.create(name=author)

        for category in categories:
            categories_in_qs = Category.objects.values()
            list_of_categories = [author['name'] for author in categories_in_qs]
            if category in list_of_categories:
                category_name = Category.objects.get(name=category)
                book.category.add(category_name)
            else:
                book.category.create(name=category)
