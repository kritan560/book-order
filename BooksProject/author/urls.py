from django.urls import path
from . import views

urlpatterns = [
    path('create-author', views.CreateAuthor.as_view(), name='create-author'),
]