from django.urls import path
from . import views


app_name = 'category'
urlpatterns = [
    path('', views.parent_category, name='parent_categories')
]
