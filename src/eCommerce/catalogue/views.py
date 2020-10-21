from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, Order, OrderItem




def basket(request):
    return render(request, 'basket.html')


def checkout(request):
    return render(request, 'checkout.html')



class HomeView(ListView):
    model = Item
    template_name = "index.html"


def add_to_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_item = OrderItem.objects

