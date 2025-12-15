from django.contrib import admin
from django.urls import path

import lots.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lots.views.lots_list),
    path('<int:id>/', lots.views.lots_detail),
]
