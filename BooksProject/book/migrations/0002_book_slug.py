# Generated by Django 4.1 on 2022-08-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
