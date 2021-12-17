from django.db import models
from datetime import datetime
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    owner_name = models.CharField(max_length=25)
    date = models.CharField(max_length=50, default=str(datetime.now()))
    type = models.CharField(max_length=1000)
