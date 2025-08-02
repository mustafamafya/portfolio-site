from django.urls import path
from . import views
from .views import products , product_page

urlpatterns = [
    path('products/', products, name='products'),
    path('product/<int:pk>/', views.product_page, name='product_page'),
]