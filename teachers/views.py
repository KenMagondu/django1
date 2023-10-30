from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    return HttpResponse("Welcome to emobilis")

def About(request):
    return HttpResponse("About emobilis ")

def Contact(request):
    return HttpResponse("I AM KEN MAGONDU A DJANGO DEV. MY CONTACTS ARE +254742689187")
