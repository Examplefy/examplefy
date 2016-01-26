from django.contrib import admin

from .models import Transaction, UserCheckout

admin.site.register(Transaction)
admin.site.register(UserCheckout)