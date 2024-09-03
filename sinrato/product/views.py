from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Product, ProductVersion, Category,  Manufacturer, Color, Images, ReviewComment
from .forms import ReviewForm
 
class ProductView(ListView):
    model = Product
    paginate_by = 8
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
    form_class = ReviewForm

    def get_object(self):
        return ProductVersion.objects.filter(pk=self.kwargs['pk']).first()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_colors = []
        product = Product.objects.get(product_version=self.get_object())
       
     
        product_versions = product.product_version.all()
        related_products = Product.objects.filter(category=product.category).exclude(product_version=self.get_object())
       
       

        for version in product_versions:
            product_colors.append({'id': version.id, 'product': version.product.id, 'color': version.color})
        
        context['colors'] = product_colors
        context['images'] = self.get_object().image.all()
        context['related'] = related_products

        return context
    
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.key = Product.objects.get(product_version=self.get_object())
            comment.save()
        return redirect('product' , pk=self.kwargs.get('pk') )
