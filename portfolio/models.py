from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class reviewed(models.Model):
    Name = models.ForeignKey(User, on_delete=models.CASCADE)
    Relationship = models.CharField(max_length=15,default=' ')
    Description = models.CharField(max_length = 100,blank=True)
    Rating = models.CharField(max_length=15,default=' ')
    Social = models.URLField(blank=True)
    Flag = models.BooleanField(default=False)
