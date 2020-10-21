from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

def home(request):
    items = Item.objects.all()

    return render(request, 'index.html', {'items': items})


def basket(request):
    return render(request, 'basket.html')


def checkout(request):
    return render(request, 'checkout.html')



class HomeView(ListView):
    model = Item
    template_name = "index.html"

