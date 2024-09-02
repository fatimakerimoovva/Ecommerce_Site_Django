from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from .models import Wishlist, Basket, Basket_item
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from product.models import *
# Create your views here.

class BasketView(LoginRequiredMixin, ListView):
    model = Basket
    template_name = 'basket.html'
    context_object_name = 'basket'
    
    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user).first()

def checkout(request):
    return render(request, 'checkout.html')


class WishlistView(LoginRequiredMixin, ListView):
    model = Wishlist
    template_name = 'wishlist.html'
    context_object_name = 'wishlist'
    
    def get_queryset(self):
       
        return  Wishlist.objects.filter(user=self.request.user).first()
    


