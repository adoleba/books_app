# Generated by Django 2.2.1 on 2019-05-14 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_import_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='import_description',
        ),
    ]
