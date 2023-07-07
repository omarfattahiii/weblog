from django.urls import path
from . import views


app_name = "config"
urlpatterns = [
    path('', views.index, name='index'),
    path('srch/', views.search, name="search"),
    path('cntct/', views.contact, name='contact'),
    path('abut/', views.about, name='about'),
    path('rfnc/', views.reference, name='references'),

    path('sbscbr/', views.subscribed, name='subscribed'),

    path('acnt/prfl/', views.profile, name='profile'),
    path('acnt/sinup/', views.signUp, name='signup'),
    path('acnt/sinin/', views.signIn, name='signin'),
    path('acnt/sinot/', views.signOut, name='signout'),
]
