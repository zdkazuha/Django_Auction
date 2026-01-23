from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from lots.models import Bid, Category, Lot, Auction
from lots.forms import AuctionForm, LotForm
from django.contrib import messages

from favorites.favorites import get_favorite_lots

# Create your views here.

def lots_index(request):
    lots = Lot.objects.all()
    auctions = Auction.objects.all()
    categories = Category.objects.all()

    lot = Lot.objects.first()

    return render(request, "lots/index.html", { 'lots' : lots, 'auctions': auctions, 'categories': categories, 'favorite_lots': get_favorite_lots(request)})

def lots_list(request):
    lots = Lot.objects.all()
    return render(request, "lots/list.html", {'lots' : lots})

def lots_detail(request, pk):
    lot = get_object_or_404(Lot, pk=pk)
    bids = lot.bids.all()

    return render(request, "lots/detail.html", {'lot' : lot, 'bids': bids})

def lots_delete(request, pk):
    lot = get_object_or_404(Lot, pk=pk)
    messages.success(request, f"Lot {lot.title} deleted successfully.")
    lot.delete()
    return redirect("lots_list")

def lots_create(request):
    categories = Category.objects.all()
    auctions = Auction.objects.all()

    if request.method == "POST":
        form = LotForm(request.POST, request.FILES)
        if form.is_valid():
            lot = form.save(commit=False)   
            lot.current_price = lot.start_price  
            lot.save()  
            messages.success(request, f"Lot {lot.title} created successfully.")
            return redirect(reverse("lots_detail", args=[lot.pk]))
        else:
            print(form.errors) 
    else:
        form = LotForm()

    return render(request, "lots/create.html", {
        'form': form,
        'categories': categories,
        'auctions': auctions
    })

def lots_update(request, pk):
    lot = get_object_or_404(Lot, pk=pk)
    categories = Category.objects.all()
    auctions = Auction.objects.all()

    if request.method == "POST":
        form = LotForm(request.POST, request.FILES, instance = lot)
        if form.is_valid():
            lot = form.save(commit=False)   
            lot.save()  
            messages.warning(request, f"Lot {lot.title} updated successfully.")
            return redirect(reverse("lots_detail", args=[lot.pk]))
        else:
            print(form.errors) 
    else:
        form = LotForm(instance = lot)

    return render(request, "lots/edit.html", {
        'form': form,
        'categories': categories,
        'auctions': auctions
    })

def lots_place_bid(request, pk):
    MIN_STEP = 10

    lot = get_object_or_404(Lot, pk=pk)

    if request.method == "POST":
        bid_price = int(request.POST.get("bid_price"))

        if bid_price <= lot.current_price + MIN_STEP:
            return render(request, "lots/components/lot_form_price.html", {
                'lot': lot,
                'error': "Bid must be higher than the current price."
            })
        
        bid = Bid.objects.create(
            lot=lot,
            amount=bid_price
        )
        bid.save()
        lot.current_price = bid_price
        lot.save()

        messages.success(request, f"Successfully placed bid on {lot.title}.")

        return redirect("lots_detail", pk=lot.pk)

    return render(request, "lots/components/lot_form_price.html", {
        'lot': lot
    })

def lots_search(request):
    lots = Lot.objects.all()
    auctions = Auction.objects.all()
    categories = Category.objects.all()

    search_text = request.GET.get('search_text')
    category = request.GET.get('category')
    auction = request.GET.get('auction')

    if auction:
        lots = lots.filter(auction_id=auction)
    if category:
        lots = lots.filter(category_id=category)
    if search_text:
        lots = lots.filter(title__icontains=search_text)

    return render(request, "lots/index.html", {'lots': lots, 'auctions': auctions, 'categories': categories, 'favorite_lots': get_favorite_lots(request)})