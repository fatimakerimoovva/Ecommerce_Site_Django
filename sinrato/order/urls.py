from django.urls import path
from .views import WishlistView, BasketView
from . import views

urlpatterns = [
    path('basket/', BasketView.as_view(), name='basket'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),  
]