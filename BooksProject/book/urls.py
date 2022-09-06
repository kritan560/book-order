from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_homepage, name='book-homepage'),
    path('create-book', views.CreateBook.as_view(), name='create-book'),
    path('book-detail/<int:pk>', views.DetailBook.as_view(), name='book-detail'),
    path('book-search/', views.book_search, name='book-search'),
    path('link-list/', views.link_list, name='link-list'),
]