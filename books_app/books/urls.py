from django.urls import path
from books_app.books.views import index, import_book, add_book

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_book, name='add_book'),
    path('import/', import_book, name='import_book'),
]
