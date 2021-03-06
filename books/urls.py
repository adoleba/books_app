from django.urls import path

from books.views import index, add_book, add_author, set_import

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_book, name='add_book'),
    path('add/author/', add_author, name='add_author'),
    path('import/', set_import, name='set_import'),
]
