from django.db import models

# Create your models here.
class aut(models.Model):
    name=models.CharField(max_length=100)
    user=models.CharField(max_length=100 , primary_key=True)
    phone=models.CharField(max_length=100)
    passw=models.CharField(max_length=100)

def __str__(self):
        return self.nm

class new(models.Model):
    adh=models.CharField(max_length=500)
    name=models.CharField(max_length=50)
    qua=models.CharField(max_length=500)
    add1=models.CharField(max_length=500)
    add2=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=50)

class deleteitem(models.Model):
    adh=models.CharField(max_length=500)
    name=models.CharField(max_length=50)
    qua=models.CharField(max_length=500)
    add1=models.CharField(max_length=500)
    add2=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=50)
    
