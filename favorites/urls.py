from django.urls import path
from . import views

import favorites.views

urlpatterns = [
    path('add/<int:lot_id>/<str:return_url>/', favorites.views.add_lot_to_favorites, name='add_lot_to_session'),
    path('remove/<int:lot_id>/<str:return_url>/', favorites.views.remove_lot_from_favorites, name='remove_lot_from_session'),
]
