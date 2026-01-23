from django.urls import path

import api.views as views

urlpatterns = [
    path('lots/', views.LotsList.as_view()), 
    path('lots/create', views.LotsList.as_view()), 
    path('lots/<int:pk>', views.LotsDetail.as_view()), 
 
]
