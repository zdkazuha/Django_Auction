from django.contrib import admin
from django.urls import include, path

import home.views

urlpatterns = [
    path('', home.views.home, name='home'),
]
