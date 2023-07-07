from django.urls import path
from . import views


app_name = 'category'
urlpatterns = [
    path('', views.parent_category, name='parent_categories'),
    path('<int:id>', views.child_category, name='child_categories'),
]
