from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat in jan")


# def february(request):
#     return HttpResponse("Wash the dishes in feb")


def monthly_challenge(request, month): # second parameter should be identical to urls path string bw <> brackets
    challenge_text = None 
    if month == "january":
        challenge_text = "Eat no meat in jan"
    elif month == "february":
        challenge_text = "Was the dishes in feb"
    elif month == "march":
        challenge_text = "Learn django in mar"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)