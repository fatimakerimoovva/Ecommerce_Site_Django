from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductVersion, Category,  Manufacturer, Color, Images
 
class ProductView(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['manufacturers'] = Manufacturer.objects.all()
        context['colors'] = Color.objects.all()
        return context




class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-details.html'
    context_object_name = 'product'
    
    def get_object(self):
        return ProductVersion.objects.filter(pk=self.kwargs['pk']).first()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_colors = []
        product = Product.objects.get(product_version = self.get_object())
        versions = product.product_version.all()
        related_product=Product.objects.filter(category=product.category).exclude(product_version=self.get_object())

        print(versions)
        for version in versions:
            product_colors.append({'id': version.id, 'product': version.product.id, 'color': version.color})
            print(product_colors)
        context['images'] = self.get_object().image.all()
        context['colors'] = product_colors
        context['related']=related_product

        return context
    