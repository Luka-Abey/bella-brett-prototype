from django.urls import path
from .views import (
    HomeView,
    basket, 
    checkout,
    add_to_cart
)


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('basket/', basket, name="basket"),
    path('checkout/', checkout, name="checkout"),
    path('add-to-cart/<id>/', add_to_cart, name='add-to-cart')
]