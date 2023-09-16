from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# functions for static urls
# def january(request):
#     return HttpResponse("This is first month of the year")

# def february(request):
#     return HttpResponse("This is second month of the year")


# function for dynamic urls:
def monthly_challenge(reques, month):
    challengeText = None
    if month == 'january':
        challengeText = "This is january"
    elif month == "feburary":
        challengeText = 'This is february'
    elif month == 'march':
        challengeText = "This is march"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challengeText)
