from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Dataset

def index(request):
    latest_dataset_list = Dataset.objects.all()
    return render(request, "dataset/index.html", {
        "latest_dataset_list": latest_dataset_list
    })

def detail(request, id):
    dataset = get_object_or_404(Dataset, pk=id)
    return render(request, "dataset/detail.html", {
        "dataset": dataset
    })