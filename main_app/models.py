from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


class Topp(models.Model):  
    player = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    highlight = models.TextField(max_length=250)
    year = models.IntegerField()
    company = models.CharField(max_length=100)
    img = models.URLField(max_length=500, default = 'Enter URL')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'topp_id': self.id})


class Joke(models.Model):
    joke = models.TextField(max_length=150)



class Offer(models.Model):
     date = models.DateField()

     price = models.DecimalField(max_digits=25, decimal_places=2, validators=[MinValueValidator(10)])

     topp = models.ForeignKey(Topp, on_delete=models.CASCADE)

     def __str__(self):
        return f"{self.price} on {self.date}"



    