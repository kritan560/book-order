from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth import urls
from django.views.generic import (
    CreateView,
    DetailView,
    View,
)
from django.urls import reverse_lazy
from comment.models import Comment
from django.contrib.auth import get_user
from django.contrib import messages

# Create your views here.
def book_homepage(request):
    # print(request.is_ajax())
    books = Book.objects.all()
    context = {'books':books, 'title':'Book Homepage'}
    return render(request, 'book/home/home.html', context)

class CreateBook(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'book/create-book/create-book.html'
    success_url = reverse_lazy('book-homepage')

# class DetailBook(DetailView):
#     model = Book
#     fields = '__all__'
#     template_name = 'book/detail-book/detail-book.html'
#     context_object_name = 'book'

class DetailBook(View):
    def get(self, request ,pk):
        # print(dir(request.user))
        # print(request.user.is_staff)
        model = Book.objects.get(id=pk)
        comment = Comment.objects.filter(comment_on=model)
        context = {'comment':comment, 'book':model}
        return render(request, 'book/detail-book/detail-book.html', context)

def book_search(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        book = Book.objects.filter(title__icontains=book_name)
        context = {'books':book}
        return render(request, 'book/search-book/search-book.html', context)

def link_list(request):
    return render(request, 'book/link-list/link-list.html')