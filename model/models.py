from ast import mod
from msilib.schema import Signature
from pickle import TRUE
from django.db import models
department_CHOICES = (
    ('Gynacology','Gynacology'),
    ('Dermatologist', 'Dermatologist'),
    ('Orthology','Orthology'),
    ('Anesthesiology','Anesthesiology'),
    ('Ayurvedic','Ayurvedic'),
)
time_CHOICES = (
    ('8:00 to 9:00','8:00 to 9:00'),
    ('9:00 to 10:00', '9:00 to 10:00'),
    ('10:00 to 1:00','10:00 to 1:00'),
)

# Create your models here.
class Patient(models.Model):
    Id = models.CharField(max_length=10, primary_key=TRUE,auto_created=True)
    UserName = models.CharField(max_length=200 ,null=True)
    Password = models.CharField(max_length=100 ,null=True)
    Phone = models.IntegerField()
    Email = models.EmailField(max_length=100,null=True)
    Address = models.CharField(max_length=100,null=True) 
    Process =  models.CharField(max_length=100,null=True)
    Disease_history = models.TextField(null=True)
    
    def __str__(self) -> str:
         return self.Id



class Charges(models.Model):
   CH_id = models.CharField(max_length=10, primary_key=TRUE)
   Name =   models.CharField(max_length=200 ,null=True)
   Amount =   models.CharField(max_length=200 ,null=True)
   Description = models.TextField(null=True)
   CodeForDiscond =  models.IntegerField()
   Total = models.CharField(max_length=200 ,null=True)
   
   def __str__(self) -> str:
         return self.CH_id


class MedicalSpecialistes(models.Model): 
    Sid = models.CharField(max_length=10, primary_key=TRUE)
    Sname = models.CharField(max_length=200 ,null=True)
    Spassword = models.CharField(max_length=100 ,null=True)
    Sphone = models.IntegerField()
    Semail = models.EmailField(max_length=100,null=True)
    Saddress = models.CharField(max_length=100,null=True) 
    Signature =  models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
         return self.Sid

class test(models.Model): 
    name = models.CharField(max_length=200 ,primary_key=TRUE)
    code = models.IntegerField()
    discription = models.TextField(max_length=300 ,null=True)
    preparations = models.CharField(max_length=200 ,null=True)
    price = models.IntegerField()
    
    def __str__(self) -> str:
         return self.name
class Book(models.Model):
        Name = models.CharField(max_length=200 ,null=True)
        Email= models.EmailField(null=True)
        Date= models.TextField(null=True)
        Time= models.CharField(max_length=200 ,null=True,choices=time_CHOICES)
        Department=models.CharField(max_length=200 ,null=True,choices=department_CHOICES)
        
        def __str__(self) -> str:
           return self.Name