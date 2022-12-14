# Generated by Django 4.1 on 2022-08-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountAuthentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField()),
                ('logo', models.ImageField(upload_to='account_authentication/logo/')),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
