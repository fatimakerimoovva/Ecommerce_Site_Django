from django.urls import path
from .views import ProductView, ProductDetailView
from . import views


urlpatterns = [
    path('product/', ProductView.as_view(), name='product'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]


