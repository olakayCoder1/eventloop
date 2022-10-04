from django.contrib import admin
from .models import (
    EventCentre, HallImage , HallPaymentCategory ,
    EventCentreCategory, Hall,
    Booking , EventCentreImage ,
)
# Register your models here.



class EventCentreImageInline(admin.TabularInline):
    model = EventCentreImage

class EventCentreAdmin(admin.ModelAdmin):

    inlines = [EventCentreImageInline]



class HallImageInline(admin.TabularInline):
    model = HallImage
class HallAdmin(admin.ModelAdmin):
    inlines = [HallImageInline]



admin.site.register(EventCentreCategory)
admin.site.register(EventCentre , EventCentreAdmin )
admin.site.register(EventCentreImage)   
admin.site.register(Booking)
admin.site.register(Hall , HallAdmin)
admin.site.register(HallImage)
admin.site.register(HallPaymentCategory)