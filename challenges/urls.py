
from django.urls import path
from . import views

urlpatterns = [
    # path for static urls
    # path("january", views.january),
    # path("february", views.february)

    path("", views.index), # this will direct the traffic with no string after /challenges/ 
    #path for dynamic urls:
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
