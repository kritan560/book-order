# Generated by Django 4.1 on 2022-08-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_author_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
