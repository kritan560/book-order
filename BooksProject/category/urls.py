from django.urls import path
from . import views

urlpatterns = [
    path('create-category', views.CreateCategory.as_view(), name='create-category'),
    path('category-detail/<int:id>', views.category_detail, name='category-detail')
]