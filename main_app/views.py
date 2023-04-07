from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request,'base.html')

def about(request):
    return render(request, 'about.html')

def topps_index(request):
    return render(request, 'topps/index.html', {'topps': topps})


class Card:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

topps = [
  Card('Lolo', 'tabby', 'foul little demon', 3),
  Card('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Card('Raven', 'black tripod', '3 legged cat', 4),
  Card('Scrappy', 'french blue', 'cuddle bug', 10),
  Card('Addie', 'golden', 'A menace', 2),
]
