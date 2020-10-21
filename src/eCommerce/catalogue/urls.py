from django.urls import path
from .views import (
    HomeView,
    basket, 
    checkout
)


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('basket/', basket, name="basket"),
    path('checkout/', checkout, name="checkout"),
]