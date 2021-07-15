from django.contrib import admin
from .models import Customer, Wine, Food, Lodge, Reservation


admin.site.register(Customer)
admin.site.register(Wine)
admin.site.register(Food)
admin.site.register(Lodge)
admin.site.register(Reservation)
