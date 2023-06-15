from django.urls import path
from . import views


app_name = "config"
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('references/', views.reference, name='reference'),
]
