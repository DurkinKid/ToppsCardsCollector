from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from datetime import date





class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} print of {Topp.player}"

    def get_absolute_url(self):
        return reverse('company_detail', kwargs={'pk': self.id})


class Topp(models.Model):  
    player = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    highlight = models.TextField(max_length=250)
    year = models.IntegerField()
    company = models.ManyToManyField(Company)
    img = models.URLField(max_length=500, default = 'Enter URL')

    def offers_made_today(self):
        return self.offer_set.filter(date=date.today()).count() >= len(Offer.price)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'topp_id': self.id})
    
    def __str__(self):
        return f"{self.player}"
    


class Joke(models.Model):
    joke = models.TextField(max_length=150)






class Offer(models.Model):
     
     date = models.DateField()

     price = models.DecimalField(max_digits=25, decimal_places=2, validators=[MinValueValidator(1)])

     topp = models.ForeignKey(Topp, on_delete=models.CASCADE)


     def __str__(self):
        return f"Offer for {self.topp.player} is {self.price} on {self.date}"



    