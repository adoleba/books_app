import django_filters

from books.models import Category, Author, Book


class QuerysetFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all().order_by('name'), label='Kategoria')
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all().order_by('name'), label='Autor')

    class Meta:
        model = Book
        fields = ['category', 'author', ]
