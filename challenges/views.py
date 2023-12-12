from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("Eat no meat in jan")


def february(request):
    return HttpResponse("Wash the dishes in feb")


def monthly_challenge(request):
    return HttpResponse()