from django.db import models
from sinrato.utils.base import BaseModel
from user.models import User
from product.models import ProductVersion



 
class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_wishlist')
    product = models.ManyToManyField(ProductVersion, related_name='product_wishlist')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.email}'s wishlist"
    
    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'
        
class Basket_item(BaseModel):
    product = models.ForeignKey(
        ProductVersion, on_delete=models.CASCADE, related_name='basket_product')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='basket_user')
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}'s  basket item"
    

    def get_subtotal(self):
        if self.product.product.in_sale:
          return self.product.product.price * self.quantity
        else:
          return self.product.product.old_price * self.quantity


    
    class Meta:
        verbose_name = 'Basket Item '
        verbose_name_plural = 'Baskets Items'
        
class Basket(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Basket_item, related_name='basket_items')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.email}'s basket"

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'
    