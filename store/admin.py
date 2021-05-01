from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'date']


@admin.register(Toppings)
class ToppingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name']