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
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qa.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity +=1 ;
            order_item.save()
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
    

