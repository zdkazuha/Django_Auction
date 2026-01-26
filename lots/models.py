from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.utils import timezone

class Auction(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)]
    )    
    image = models.ImageField(
        upload_to='auction_image/',
        null=True,
        blank=True
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.start_time} : {self.end_time}'

class Category(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return self.title

class Lot(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)]
    )
    description = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(10)]
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='owned_lots'
    )
    buyer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='purchased_lots'
    )
    auction = models.ForeignKey(
        Auction,
        on_delete=models.CASCADE,
        related_name='lots'
    )
    image = models.ImageField(
        upload_to='lot_image/',
        null=True,
        blank=True
    )
    start_price = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    current_price = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    end_price = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )

    def __str__(self):
        return f'{self.title} : {self.description}'
    
class Bid(models.Model):
    lot = models.ForeignKey(
        Lot,
        on_delete=models.CASCADE,
        related_name='bids'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(
        validators=[MinValueValidator(10)]
    )
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} → {self.amount} on {self.lot}'