from django.contrib import admin
from .models import MenuItem, Booking
import Restaurant

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Booking)