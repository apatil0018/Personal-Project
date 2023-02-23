from django.conf import settings
from django.db import models

# Create your models here
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='image/')
    report = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name
