from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from lots.models import Category, Lot, Auction
from lots.forms import LotForm

# Create your views here.

def lots_list(request):
    lots = Lot.objects.all()
    return render(request, "lots/list.html", {'lots' : lots})


def lots_detail(request, pk):
    lot = get_object_or_404(Lot, pk=pk)
    return render(request, "lots/detail.html", {'lot' : lot})

def lots_delete(request, pk):
    lot = get_object_or_404(Lot, pk=pk)
    lot.delete()
    return redirect("lots_list")

def lots_create(request):
    categories = Category.objects.all()
    auctions = Auction.objects.all()

    if request.method == "POST":
        form = LotForm(request.POST)
        if form.is_valid():
            lot = form.save(commit=False)   
            lot.current_price = lot.start_price  
            lot.save()  
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
