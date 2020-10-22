from django.urls import path
from .views import (
    HomeView,
    BasketView, 
    checkout,
    add_to_cart
)

app_name = "catalogue"

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('basket/', BasketView.as_view(), name="basket"),
    path('checkout/', checkout, name="checkout"),
    path('add-to-cart/<id>/', add_to_cart, name='add-to-cart')
]