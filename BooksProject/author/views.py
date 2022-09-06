from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView
)
from .models import Author
# Create your views here.
class CreateAuthor(CreateView):
    model = Author
    fields = '__all__'
    template_name = 'author/create-author/create-author.html'
    success_url = reverse_lazy('book-homepage')