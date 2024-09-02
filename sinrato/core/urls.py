from django.urls import path
from . import views
from .views import  SearchView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
     path('search/' , SearchView.as_view() , name = 'search'),
]