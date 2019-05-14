from django.urls import path
from books_app.books.views import index, import_book, add_book, add_author

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_book, name='add_book'),
    path('add/author/', add_author, name='add_author'),
    path('import/', import_book, name='import_book'),
]
