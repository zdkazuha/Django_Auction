FAVORITES_LOTS_KEY = 'favorite_lots'

def get_favorite_lots(request):
    return request.session.get(FAVORITES_LOTS_KEY, [])

def get_count_of_favorite_lots(request):
    return len(get_favorite_lots(request))

def add_to_favorites(request, lot_id):
    favorites = request.session.get(FAVORITES_LOTS_KEY, [])

    if lot_id not in favorites:
        favorites.append(lot_id)
        request.session[FAVORITES_LOTS_KEY] = favorites

    request.session.modified = True

def remove_from_favorites(request, lot_id):
    favorites = request.session.get(FAVORITES_LOTS_KEY, [])

    if lot_id in favorites:
        favorites.remove(lot_id)
        request.session[FAVORITES_LOTS_KEY] = favorites

    request.session.modified = True