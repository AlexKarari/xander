from django.db import models

# Create your models here.
class Image(models.Model):
    about = models.CharField(max_length=10000)
    my_image = models.ImageField(upload_to='avatar/')


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    link = models.CharField(max_length=100)
