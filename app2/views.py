from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to Index of app2</h1>")


def sample(request):
    return render(request,"sample2.html")

def carry_data(request,city):
    return HttpResponse(f'<h1>The city is {city}</h1>')

