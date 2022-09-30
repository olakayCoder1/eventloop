from django.http import HttpResponse
from django.shortcuts import render
from centre.models import EventCentre , EventCentreImage , Booking
# Create your views here.


def home(request):
    for model in Booking.objects.all():
        model.delete()

    for model in EventCentreImage.objects.all():
        print(model.event_centre)
    return HttpResponse('HELLO WORLD')