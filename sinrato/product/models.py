from django.db import models
from django.urls import reverse
from sinrato.utils.base import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title

class Color(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='color_image')
    
    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
    
    def __str__(self):
        return self.name
    
class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'
    
    def __str__(self):
        return self.name

class Images(BaseModel):
    image = models.ImageField(upload_to='product_image')
    title = models.CharField(max_length=255, verbose_name='product title')
    
    def __str__(self):
        return self.title
    

class Product(BaseModel):
    title = models.CharField(max_length=255, verbose_name='product title')
    old_price = models.PositiveIntegerField(null = True, blank=True)
    in_sale = models.BooleanField(default=False)
    price = models.PositiveIntegerField(null = True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, max_length=255, related_name='product_category')
    manufacturer = models.ForeignKey(
        Manufacturer,  on_delete=models.CASCADE, related_name='product_manufacturer')
    new = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False, verbose_name='is published?')
    
    class Meta:
        verbose_name = 'Product '
        verbose_name_plural = 'Product '

    @property
    def total_quantity(self):
        return sum([versions.quantity for versions in self.product_version.all()])
    
    @property
    def get_version(self):
        for version in self.product_version.all():
            return version.pk
    
    def get_absolute_url(self):
        return reverse('api_product', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title
        
class ProductVersion(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_version')
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, max_length=255, related_name='product_version_color')
    cover_image = models.ImageField(upload_to='product_images/', blank=False)
    image = models.ManyToManyField(Images, related_name='detailimage')
    in_stock = models.BooleanField(default=False)
    quantity = models.IntegerField(verbose_name='Quantity of the product', blank=True, null=True, default=0)

    def get_absolute_url(self):
        return reverse('api_product', kwargs={"pk": self.product.pk})


    def __str__(self):
        return f"{self.product.title}'s {self.color.name} version"
     
    class Meta:
        verbose_name = 'Product version'
        verbose_name_plural = 'Product versions'

    
class ReviewComment(BaseModel):
    
    quality = models.PositiveBigIntegerField()
    price = models.PositiveBigIntegerField()
    value = models.PositiveBigIntegerField()

    nickname = models.CharField(max_length=100 , verbose_name='Nickname' )
    summary = models.CharField(max_length=100 , verbose_name='Nickname' )
    review =  models.TextField()
    key = models.ForeignKey('product.Product' ,on_delete=models.CASCADE , related_name= 'product_review')


    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    
    def __str__(self):
        return self.nickname 

#     from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.forms.widgets import RadioSelect
# from choicebtn.models import myChoice


# class myChoiceForm(UserCreationForm):
#     name=forms.CharField(max_length=55)
#     TYPE_SELECT = (('0', 'Female'),('1', 'male'),)
#     gender=forms.ChoiceField(widgets.RadioSelect(choices=TYPE_SELECT))

#     class Meta:
#            model = myChoice
#            fields = ['name','gender']
    
    
    
    