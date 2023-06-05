from django.urls import path
from . import views


app_name = 'advertising'
urlpatterns = [
    path('', views.advertising, name='advertisings')
]
