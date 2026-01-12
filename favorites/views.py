from django.shortcuts import redirect, render
FAVORITES_LOTS_KEY = 'favorite_lots'

from lots.models import Lot
from favorites.favorites import add_to_favorites, remove_from_favorites

def index(request):
    lots = Lot.objects.all()
    favorites_ids = request.session.get(FAVORITES_LOTS_KEY, [])

    lots = [lot for lot in lots if lot.id in favorites_ids]

    return render(request, "favorites/index.html", {'lots': lots})

def add_lot_to_favorites(request, lot_id, return_url):
    add_to_favorites(request, lot_id)
    return redirect(return_url)

def remove_lot_from_favorites(request, lot_id, return_url):
    remove_from_favorites(request, lot_id)
    return redirect(return_url)
    