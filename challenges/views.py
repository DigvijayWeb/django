from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("This is first month of the year")

def february(request):
    return HttpResponse("This is second month of the year")
