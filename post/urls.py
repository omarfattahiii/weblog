from django.urls import path
from . import views


app_name = "post"
urlpatterns = [
    # path('', views.posts, name="posts"),
    path('single/', views.single_posts, name="single_posts"),
    path('single/<int:id>/', views.single_posts_detail, name="single_posts_detail"),
    path('serie/', views.serie_posts, name="serie_posts"),
    path('serie/<int:id>/', views.serie_posts_detail, name="serie_posts_detail"),
    path('serie/<int:id>/<int:part_id>/', views.serie_posts_parts_detail, name="serie_posts_parts_detail"),

    path('posts/up_req/<title>/', views.update_request_post, name='update_request_post'),
]
