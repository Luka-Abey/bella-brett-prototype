from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, Order, OrderItem
from django.http import JsonResponse
import json

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


def updateItem(request):
    data = json.loads(request.body)
    itemId = data['itemId']
    action = data['action']
    print(action, itemId)

    customer = request.user.customer
    item = Item.objects.get(id = itemId)
    order, created = Order.objects.get_or_create(
        customer=customer, ordered=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, item = item)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)
        
    
    

