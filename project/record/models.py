from django.db import models

# Create your models here.
class aut(models.Model):
    nm=models.CharField(max_length=50)
    pho=models.CharField(max_length=50 ,primary_key=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.nm


class deta(models.Model):
    adh=models.CharField(max_length=500 ,primary_key=True)
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