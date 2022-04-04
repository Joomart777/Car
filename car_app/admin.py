from django.contrib import admin

# Register your models here.
from car_app.models import *

admin.site.register(Brand)
admin.site.register(Car)