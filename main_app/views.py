from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Topp
from .models import Joke
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import OfferForm

class ToppCreate(CreateView):
    model = Topp
    fields = '__all__' # all fields

class ToppUpdate(UpdateView):
    model = Topp
    fields = '__all__'

class ToppDelete(DeleteView):
    model = Topp
    success_url = '/cats/'


def add_offer(request, topp_id):
    form = OfferForm(request.POST)
    if form.is_valid():
        new_offer= form.save(commit=False)
        new_offer.topp_id = topp_id
        new_offer.save()
    return redirect('detail', topp_id=topp_id)



def home(request):
    jokes = Joke.objects.all()
    return render(request, 'home.html', {'jokes': jokes})


def base(request):
    return render(request,'base.html')

def about(request):
    return render(request, 'about.html')

def topps_index(request):
    topps = Topp.objects.all()
    return render(request, 'topps/index.html', {'topps': topps})

def topps_detail(request, topp_id):
    topp = Topp.objects.get(id=topp_id)

    offer_form = OfferForm()
    return render(request, 'topps/detail.html', {'topp': topp, 'offer_form':offer_form})


