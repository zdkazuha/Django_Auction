from django.urls import path
from . import views

urlpatterns = [
    path('', views.lots_list, name="lots_list"), 
    path('create/', views.lots_create, name="lots_create"),  
    path('delete/<int:pk>/', views.lots_delete, name="lots_delete"),  
    path('<int:pk>/', views.lots_detail, name="lots_detail"),
]
