from unicodedata import name
from django.contrib import admin
from django.urls import path
from homeapp import views

urlpatterns = [
    path('',views.login,name='login'),
    path('home',views.index,name='home'),
    path('DataEntry',views.entry_form,name='entry_form'),
    path('DataAccess',views.access_form,name='access_form'),
    path('DataDeletion',views.delete_form,name='delete_form'),
    path('convertToCSV',views.csv_convertion,name='csv_convertion'),
    path('Login',views.login,name='login')
]
