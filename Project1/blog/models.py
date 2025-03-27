from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.


class Posts_db(models.Model):

    title = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    banner = models.ImageField(
        upload_to='banners/', default='fallback.png', blank=True)
    slug = AutoSlugField(
        populate_from='title', unique=True)

    def __str__(self):
        return self.title
