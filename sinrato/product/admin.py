from django.contrib import admin

from .models import Product,Category,Images,Manufacturer,Color, ProductVersion

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Images)
admin.site.register(Manufacturer)
admin.site.register(Color)
admin.site.register(ProductVersion)
