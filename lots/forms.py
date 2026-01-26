from django import forms
from .models import Auction, Lot

class LotForm(forms.ModelForm):
    class Meta:
        model = Lot
        fields = ['title', 'image', 'description', 'category', 'auction', 'start_price']

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['title', 'image', 'start_time', 'end_time']