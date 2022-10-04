from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.

 
def home(request):
        
    return HttpResponse('HELLO WORLD')