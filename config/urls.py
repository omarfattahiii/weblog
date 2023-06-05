from django.urls import path
from . import views


app_name = "config"
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.index, name='contact'),
    path('about/', views.index, name='about'),
]
