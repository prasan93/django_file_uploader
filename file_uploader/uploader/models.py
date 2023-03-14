from django.db import models

# Create your models here.
class image_uploader(models.Model):
    title = models.CharField(max_length=100)
    file = models.ImageField(upload_to='images')
