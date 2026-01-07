from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from lots.models import Category, Lot, Auction
from lots.forms import LotForm
from django.contrib import messages

# Create your views here.

def lots_list(request):
    lots = Lot.objects.all()
    return render(request, "lots/list.html", {'lots' : lots})


def lots_detail(request, pk):
    lot = get_object_or_404(Lot, pk=pk)
    return render(request, "lots/detail.html", {'lot' : lot})

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