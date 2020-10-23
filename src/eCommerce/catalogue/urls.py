from django.urls import path
from .views import (
    HomeView,
    basket, 
    checkout,
    updateItem,
)

app_name = "catalogue"

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('basket/', basket, name="basket"),
    path('checkout/', checkout, name="checkout"),
    path('update_item/', updateItem, name='update_item')
]