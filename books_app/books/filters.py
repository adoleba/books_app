import django_filters

from books_app.books.models import Book, Category, Author


class CategoryFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Kategoria')
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all(), label='Autor')

    class Meta:
        model = Book
        fields = ['category', 'author', ]
