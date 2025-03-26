from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product  # Import the Product model
from .models import Order, OrderItem
admin.site.register(Product)  # Register the model
admin.site.register(Order)
admin.site.register(OrderItem)