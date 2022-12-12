import datetime
from django.db import models
from users.models import User
from django.utils import timezone

class Dataset(models.Model):
    title = models.CharField(max_length=80)
    slug_title = models.SlugField

    code = models.TextField(blank=False)
    about = models.TextField(blank=False)
    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    num_downloads = models.IntegerField(default=0)

    posted_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dataset = models.ForeignKey(Dataset, related_name='likes', on_delete=models.CASCADE)
