from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=100
    )
    logo = models.FileField(
        upload_to='logo/'
    )
    location = models.TextField(
        max_length=500
    )
    instagram = models.URLField()
    
