from django.urls import path
from .views import home, basket, checkout


urlpatterns = [
    path('', home, name='index'),
    path('basket/', basket, name="basket"),
    path('checkout/', checkout, name="checkout"),
]