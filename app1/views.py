from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to Index of app1</h1>")


def sample(request):
    return render(request,"sample1.html")

def carry_data(request,name):
    return HttpResponse(f'<h1>The name is {name}</h1>')
