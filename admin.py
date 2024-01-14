from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Card)
admin.site.register(MethodToPay)
admin.site.register(Reciver)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Employee)