from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("this is the home")

def detail(request, id):
    return HttpResponse(f"Estás viendo el dataset número {id}")