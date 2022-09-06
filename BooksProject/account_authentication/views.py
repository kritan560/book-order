from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse

# Create your views here.
class CreateUser(CreateView, SuccessMessageMixin):
    form_class = UserCreationForm
    template_name = 'account/user-creation/user-creation.html'
    success_url = reverse_lazy('book-homepage')
    success_message = 'Account Created Successfully'

# def favicon_icon(request):
#     return HttpResponse("<link rel='icon' href='{% static 'icon/favicon.ico' %}'>")