from django.db import models

# Create your models here.

class mobile(models.Model):
    brand=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    colour=models.CharField(max_length=50)
    price=models.IntegerField()
    memory=models.IntegerField()
    image=models.ImageField(upload_to='mobiles')



class amazon(models.Model):
    brand=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    colour=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    memory=models.IntegerField()
    image=models.ImageField(upload_to='amazon')
