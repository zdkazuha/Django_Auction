from favorites.favorites import get_count_of_favorite_lots

def favorites_lots_count(request):
    return {'favorite_count': get_count_of_favorite_lots(request)}