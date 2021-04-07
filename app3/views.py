from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to Index of app3</h1>")


def sample(request):
    return render(request,"sample3.html")

def facto(request,num):
    fact=1
    for i in range(int(num),1,-1):
        fact*=i
    return HttpResponse(f'<h2>the factorial of {num} is {fact}</h2>')