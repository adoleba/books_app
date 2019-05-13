from django.urls import path
from books_app.books.views import index, add_book, import_book, category_filter

urlpatterns = [
    path('', index),
    path('add/', add_book, name='add_book'),
    path('import/', import_book, name='import_book'),
    path('filter/', category_filter, name='category_filter')
]