from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.make_comment, name='comment'),
    path('comment/<int:pk>', views.DetailBook.as_view(), name='comment-login')
]