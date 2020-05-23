from django.contrib import admin  
from django.urls import path  
from .views import CarView
  
app_name = 'carlist' 

urlpatterns = [  
    #path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', CarView.as_view(), name='car_list'),
]