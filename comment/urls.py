from django.urls import path
from . import views


app_name = "comment"
urlpatterns = [
    path('comments/single_posts/submit/<int:id>/', views.single_comments, name='single_comments'),
    path('comments/serie_posts/submit/<int:id>/', views.serie_comments, name='serie_comments'),
]
