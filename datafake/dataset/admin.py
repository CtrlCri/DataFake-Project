# Django
from django.contrib import admin

# Models
from .models import Dataset, Like

class DatasetAdmin(admin.ModelAdmin):
    fields = [ "code", "title", "about"] 

# Register
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(Like)

