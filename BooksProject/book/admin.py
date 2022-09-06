from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['authors', 'categorys','title', 'page_num', 'image', 'price']
    prepopulated_fields = {'slug': ['title']}