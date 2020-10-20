from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def basket(request):
    return render(request, 'basket.html')


def checkout(request):
    return render(request, 'checkout.html')