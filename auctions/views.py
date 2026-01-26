from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from favorites.favorites import get_favorite_lots
from lots.models import Auction, Lot
from lots.forms import AuctionForm

# Create your views here.

def auctions_index(request):
    auctions = Auction.objects.all()

    return render(request, "auctions/index.html", {'auctions': auctions})

def auctions_list(request):
    auctions = Auction.objects.all()

    return render(request, "auctions/list.html", {'auctions': auctions})

def auctions_detail(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    lots = Lot.objects.filter(auction=auction)

    return render(request, "auctions/detail.html", {'favorite_lots': get_favorite_lots(request), 'auction': auction, 'lots': lots})

def auctions_create(request):
    if request.method == "POST":
        form = AuctionForm(request.POST, request.FILES)
        if form.is_valid():
            auction = form.save(commit=False)
            if auction.start_time < auction.end_time:
                auction.save()
                messages.success(request, f"Auction {auction.title} created successfully.")
                return redirect(reverse("auctions_detail", args=[auction.pk]))
            else:
                messages.error(request, "End time must be after start time.")
        else:
            print(form.errors)
    else:
        auction = AuctionForm()

    return render(request, "auctions/create.html", {'form': auction})

def auctions_update(request, pk):
    auction = get_object_or_404(Auction, pk=pk)

    if request.method == "POST":
        form = AuctionForm(request.POST, request.FILES, instance=auction)
        if form.is_valid():
            auction = form.save(commit=False)
            if auction.start_time < auction.end_time:
                auction.save()
                messages.warning(request, f"Auction {auction.title} updated successfully.")
                return redirect(reverse("auctions_detail", args=[auction.pk]))
            else:
                messages.error(request, "End time must be after start time.")
        else:
            print(form.errors)
    else:
        form = AuctionForm(instance=auction)

    return render(request, "auctions/edit.html", {'form': form})

def auctions_delete(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    messages.success(request, f"Auction {auction.title} deleted successfully.")
    auction.delete()
    return redirect("auctions_list")

def auctions_search(request):
    search_text = request.GET.get("search_text")
    auctions = Auction.objects.all()

    if search_text:
        auctions = auctions.filter(title__icontains=search_text)

    return render(request, "auctions/index.html", {'auctions': auctions, 'search_text': search_text})