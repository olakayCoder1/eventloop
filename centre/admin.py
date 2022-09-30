from django.contrib import admin
from .models import (
    EventCentre,
    EventCentreCategory,
    Booking , EventCentreImage
)
# Register your models here.



admin.site.register(EventCentreCategory)
admin.site.register(EventCentre)
admin.site.register(EventCentreImage)   
admin.site.register(Booking)