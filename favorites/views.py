from django.shortcuts import redirect, render
FAVORITES_LOTS_KEY = 'favorite_lots'

from favorites.favorites import add_to_favorites, remove_from_favorites

def add_lot_to_favorites(request, lot_id, return_url):
    add_to_favorites(request, lot_id)
    return redirect(return_url)

def remove_lot_from_favorites(request, lot_id, return_url):
    remove_from_favorites(request, lot_id)
    return redirect(return_url)
    