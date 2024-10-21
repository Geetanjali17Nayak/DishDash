from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
     peoples=[{'name': "Geetanjali" , 'age': int('21')}, 
	             {'name': "Ayush" , 'age':int('21')}]
     
     return render(request, "ind.html", context = {'peoples' : peoples})

