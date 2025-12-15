from django.shortcuts import render, redirect, get_object_or_404
from lots.models import Lot

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
    return redirect("/lots/")