from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}



# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
                      "months" : months,
                  })

    # for month in months:
    #     capital_month = month.upper()
    #     month_path = reverse("month-challenge", args=[month]) # month-challenge is defined in url path in urls.py
    #     list_items+= f"<li><a href=\"{month_path}\">{capital_month}</a></li>"
    
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

# functions for static urls
# def january(request):
#     return HttpResponse("This is first month of the year")

# def february(request):
#     return HttpResponse("This is second month of the year")


# function for dynamic urls:
def monthly_challenge(request, month):
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
        #response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "month" : month,
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()
    



def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month]) # challenge/january
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This is not a supported month")
    
