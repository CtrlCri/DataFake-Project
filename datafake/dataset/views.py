from django.shortcuts import render
from django.http import HttpResponse

from .models import Dataset

def index(request):
    latest_dataset_list = Dataset.objects.all()
    return render(request, "dataset/index.html", {
        "latest_dataset_list": latest_dataset_list
    })

def detail(request, id):
    return HttpResponse(f"Estás viendo el dataset número {id}")