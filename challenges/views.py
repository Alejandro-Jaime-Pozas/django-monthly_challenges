from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse # reverse allows to reference url paths defined in urls.py


monthly_challenges = {
    "january": "Eat no meat in jan",
    "february": "Was the dishes in feb",
    "march": "Learn django in mar",
    "april": "Eat no meat in jan",
    "may": "Was the dishes in feb",
    "june": "Learn django in mar",
    "july": "Eat no meat in jan",
    "august": "Was the dishes in feb",
    "september": "Learn django in mar",
    "october": "Eat no meat in jan",
    "november": "Was the dishes in feb",
    "december": "Learn django in mar",
}

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat in jan")


# def february(request):
#     return HttpResponse("Wash the dishes in feb")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenges/january; args is the month string you want to redirect to; reverse allows us to reference a urls.py path
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month): # second parameter should be identical to urls path string bw <> brackets
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)