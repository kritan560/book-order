from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.place_order, name='place-order'),
    path('order-detail', views.order_detail, name='order-detail'),
]