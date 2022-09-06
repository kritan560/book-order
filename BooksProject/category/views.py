from django.shortcuts import render
from django.views.generic import (
    CreateView,
)
from django.urls import reverse_lazy
from . models import Category
from book.models import Book

# Create your views here.
class CreateCategory(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'category/create-category/create-category.html'
    success_url = reverse_lazy('book-homepage')

def category_detail(request, id):
    category = Category.objects.get(id=id)
    book = Book.objects.filter(category=category)
    context = {'books':book}
    return render(request, 'category/category-detail/category-detail.html', context)