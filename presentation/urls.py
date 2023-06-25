from django.urls import path
from . import views


app_name = 'presentation'
urlpatterns = [
    path('', views.presentation, name='presentations'),
    path('<int:id>/', views.presentation_detail, name='presentation_detail'),
]
