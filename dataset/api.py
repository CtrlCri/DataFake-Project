from .models import Dataset
from rest_framework import (
    viewsets,
    authentication,
    permissions,
    filters
)
from .serializers import DatasetSerializer

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer