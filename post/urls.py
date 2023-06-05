from django.urls import path
from . import views


app_name = "post"
urlpatterns = [
    path('single/', views.single_posts, name="single_posts"),
    path('serie/', views.serie_posts, name="serie_posts"),
]
