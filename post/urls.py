from django.urls import path
from . import views


app_name = "post"
urlpatterns = [
    path('', views.posts, name="posts"),
    path('single/', views.single_posts, name="single_posts"),
    path('single/<int:pk>/', views.single_posts_detail, name="single_posts_detail"),
    path('serie/', views.serie_posts, name="serie_posts"),
    path('serie/<int:pk>/', views.serie_posts_detail, name="serie_posts_detail"),
]
