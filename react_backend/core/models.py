from django.db import models

# Create your models here.

class Patient(models.Model):
    username = models.CharField(blank=False,null=False,verbose_name='username',unique=True,max_length=100,primary_key=True)
    password = models.CharField(blank=False,null=False,verbose_name='password',unique=True,max_length=100)


class Doctor(models.Model):
    id = models.IntegerField(blank=False,null=False,verbose_name='id',primary_key=True)
    rating = models.FloatField(blank=False,null=False,verbose_name='rating')
    numberOfVoters = models.IntegerField(blank=False,null=False,verbose_name='numberOfVoters')