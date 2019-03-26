from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index1(request):
   template= loader.get_template('weather/index1.html')
   context={

   }
   return HttpResponse(template.render(context,request))

def index(request):
    return HttpResponse("Weather of Kathmandu is :")
def index2(request):
    return HttpResponse("Weather of Pokhara is :")