from django.contrib import admin
from .models import Item, Order, OrderItem


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = [
        'name',
        'price',
        'discount_price'
    ]


admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)