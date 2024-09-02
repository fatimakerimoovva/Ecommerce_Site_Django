from django.urls import path 
from .views import WishlistAPIView, BasketApiView

urlpatterns = [
    path('api/wishlist/',  WishlistAPIView.as_view() , name = 'api_wishlist'),
    path('api/basket/' , BasketApiView.as_view() , name = 'api_basket'),
]