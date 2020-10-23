from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, Order, OrderItem
from django.http import JsonResponse

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False) 
        items = order.orderitem_set.all()
    else:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0
        }

    context = {'items': items, 'order': order}   
    return render(request, 'checkout.html', context)


def basket(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False) 
        items = order.orderitem_set.all()
    else:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0
        }

    context = {'items': items, 'order': order}   
    return render(request, 'basket.html', context)


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


        
    

