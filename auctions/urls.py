from django.urls import path
from . import views

urlpatterns = [
    path('', views.auctions_index, name="auctions_index"),
    path('list/', views.auctions_list, name="auctions_list"),
    path('search/', views.auctions_search, name="auctions_search"),
    path('create/', views.auctions_create, name="auctions_create"),
    path('<int:pk>/', views.auctions_detail, name="auctions_detail"),
    path('edit/<int:pk>/', views.auctions_update, name="auctions_update"),
    path('delete/<int:pk>/', views.auctions_delete, name="auctions_delete"),
]



