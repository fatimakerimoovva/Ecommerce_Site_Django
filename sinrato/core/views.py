from django.shortcuts import render
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import CreateView, ListView
# from .models import Core,ContactUs
from product.models import Category,Product
from blog.models import Blogs
# from .form import ContacUsForm
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


class SearchView(ListView):
    model=Product
    template_name='search.html'
    context_object_name='products'
    
    def get_queryset(self):
        product=self.request.GET.get('name')
        if product:
            multiple=Product.objects.filter(Q(title__icontains=product))
        else:
            multiple = Product.objects.all()
        return multiple