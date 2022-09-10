from django.db import models

# Create your models here.

class List(models.Model):
    heading = models.CharField(max_length=200,default="")
    description = models.CharField(max_length=500,default="")
    status = models.CharField(max_length=200,default="")
    date = models.DateField


    def __str__(self):
        return self.heading 


