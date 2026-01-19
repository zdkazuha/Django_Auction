from django.urls import path
from . import views

urlpatterns = [
    path('', views.lots_index, name="lots_index"), 
    path('list/', views.lots_list, name="lots_list"), 
    path('create/', views.lots_create, name="lots_create"),  
    path('<int:pk>/', views.lots_detail, name="lots_detail"),
    path('edit/<int:pk>', views.lots_update, name="lots_update"),  
    path('lots/<int:pk>/bid/', views.place_bid, name="place_bid"),
    path('delete/<int:pk>/', views.lots_delete, name="lots_delete"),  
]
