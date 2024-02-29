from django.shortcuts import render
from django .http import HttpResponse

# Create your views here.
def home(requests):
    return HttpResponse("Welcome to our home page")
def contacts (request):
    return HttpResponse("This is  our contact info")
def courses (request):
    return HttpResponse("We offer these courses")
def location (request):
    return HttpResponse("We are located here")
