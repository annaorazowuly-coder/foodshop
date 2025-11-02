from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('category/<str:category_name>/', views.category_view, name='category_view'),
]
