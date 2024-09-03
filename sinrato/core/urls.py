from django.urls import path
from . import views
from .views import  SearchView, IndexView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('search/' , SearchView.as_view() , name = 'search'),
    path('',IndexView.as_view(),name='index'),

]