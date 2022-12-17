from rest_framework import serializers
from .models import Dataset

class DatasetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dataset
        #fields = '__all__'
        fields = ('id', 'title', 'code', 'about', 'created_at', 'updated_at', 'num_downloads', 'posted_by')