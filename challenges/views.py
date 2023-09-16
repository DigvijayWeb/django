from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "This is first month",
    "february": "This is second month",
    "march": "This is third month",
    "april": "This is fourth month",
    "may": "This is fifth month",
    "june": "This is sixth month",
    "july": "This is seventh month",
    "august": "This is eighth month",
    "september": "This is nineth month",
    "october": "This is tenth month",
    "november": "This is eleventh month",
    "december": "This is twelveth month"
}


# Create your views here.

# functions for static urls
# def january(request):
#     return HttpResponse("This is first month of the year")

# def february(request):
#     return HttpResponse("This is second month of the year")


# function for dynamic urls:
def monthly_challenge(reques, month):
    # challengeText = None
    # if month == 'january':
    #     challengeText = "This is january"
    # elif month == "feburary":
    #     challengeText = 'This is february'
    # elif month == 'march':
    #     challengeText = "This is march"
    # else:
    #     return HttpResponseNotFound("This month is not supported!")
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
    



def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month]) # challenge/january
        return HttpResponseRedirect("/challenges/" + redirect_month)
    except:
        return HttpResponseNotFound("This is not a supported month")
    
