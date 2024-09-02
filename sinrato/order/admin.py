from django.contrib import admin

# Register your models here.
from .models import Wishlist,Basket_item,Basket

admin.site.register(Wishlist)
admin.site.register(Basket_item)
admin.site.register(Basket)