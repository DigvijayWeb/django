
from django.urls import path
from . import views

urlpatterns = [
    # path for static urls
    # path("january", views.january),
    # path("february", views.february)

    #path for dynamic urls:
    path("<month>", views.monthly_challenge)
]
