from django.urls import path
from . import views


app_name = "config"
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name="search"),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('references/', views.reference, name='references'),

    path('account/signup/', views.signUp, name='signup'),
    path('account/signin/', views.signIn, name='signin'),
    path('account/signout/', views.signOut, name='signout'),
]
