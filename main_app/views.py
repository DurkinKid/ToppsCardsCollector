from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {'jokes': jokes})

def base(request):
    return render(request,'base.html')

def about(request):
    return render(request, 'about.html')

def topps_index(request):
    return render(request, 'topps/index.html', {'topps': topps})


class Topp:  
  def __init__(self, player, team, position, highlight, year, company, img):
    self.player = player
    self.team = team
    self.position = position
    self.highlight = highlight
    self.year = year
    self.company = company
    self.img = img

topps = [
  Topp('Mickey Mantle', 'Yankees', 'Center Field / First Base', 'Batted .285, hit 31 home runs, and knocked in 75 ribeyes!', 1959, 'Topps', 'https://cdn5.mavin.io/production/soldItems/261479769/images/image-gallery.jpg'),
  Topp('Carl Yastrzemski', 'Red Sox', 'Left Field', 'Batted .321, hit 14 home runs, and knocked in 68 ribeyes!', 1963, 'Topps', 'https://i.ebayimg.com/images/g/CfUAAOSwbVZkER8q/s-l500.png'),
  Topp('Yogi Berra', 'Yankees', 'Catcher', 'Batted .272, hit 27 home runs, and knocked in 108 ribeyes!', 1955, 'Topps', 'https://i.psacard.com/cardfacts/1955-topps-198-yogi-berra-27467.jpg?h=1000')
]

class Joke:
   def __init__(self, joke):
      self.joke = joke

jokes = [
    Joke('If Babe Ruth married Betty Crocker, Do you think he would be a better badder?')
]