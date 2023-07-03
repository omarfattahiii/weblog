from django.urls import path
from . import views


app_name = "post"
urlpatterns = [
    # path('', views.posts, name="posts"),
    path('sngls/', views.single_posts, name="single_posts"),
    path('sngls/<int:id>/', views.single_posts_detail, name="single_posts_detail"),
    path('sres/', views.serie_posts, name="serie_posts"),
    path('sres/<int:id>/', views.serie_posts_detail, name="serie_posts_detail"),
    path('sres/<int:id>/<int:part_id>/', views.serie_posts_parts_detail, name="serie_posts_parts_detail"),

    path('psts/up_req/<title>/', views.update_request_post, name='update_request_post'),
]
