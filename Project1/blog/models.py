from django.db import models

# Create your models here.


class Posts_db(models.Model):

    title = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title
