from django.db import models

# Create your models here.

class lots(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    start_price = models.IntegerField()
    current_price = models.IntegerField()
    end_price = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {self.description}'
