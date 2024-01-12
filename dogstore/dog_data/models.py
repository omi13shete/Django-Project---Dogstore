from django.db import models
import datetime

# Create your models here.

class inquiry(models.Model):

    name=models.CharField( max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class addnewpet(models.Model):
    pet_id = models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=50)
    breed=models.CharField(max_length=50)
    sex=models.CharField(max_length=10)
    color=models.CharField(max_length=50)
    image=models.ImageField( upload_to="image/")


    def __str__(self):
        return self.name










