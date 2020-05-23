from django.contrib import admin
from carlist.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("manufacturer", "car_model", "year")