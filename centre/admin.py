from django.contrib import admin
from .models import (
    EventCentre,
    EventCentreCategory,
    Booking
)
# Register your models here.



admin.site.register(EventCentreCategory)
admin.site.register(EventCentre)
admin.site.register(Booking)