# Django
from django.contrib import admin

# Models
from dataset.models import Dataset, Like

# Register
admin.site.register(Dataset)
admin.site.register(Like)

