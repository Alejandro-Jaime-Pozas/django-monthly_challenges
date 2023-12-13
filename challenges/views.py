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


# create a main index with all the months as html links
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month]) # ref month-challenge path
        list_items += f"<li><h3><a href=\"{month_path}\">{month.capitalize()}</a></h3></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


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
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data) 
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")