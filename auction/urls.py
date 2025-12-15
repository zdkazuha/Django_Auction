from django.contrib import admin
from django.urls import include, path

import lots.views

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('lots/', include('lots.urls')),
]
