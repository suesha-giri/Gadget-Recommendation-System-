from django.db import models

# Create your models here.

class Mobile(models.Model):
   # id= int..automatically created
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    price= models.IntegerField()


class Smartphone(models.Model):
   name= models.CharField(max_length=100)
   img= models.ImageField(upload_to='pics')
   price= models.IntegerField()


class SmartphoneDetails(models.Model):
   smartphone=models.ForeignKey(Smartphone, on_delete=models.CASCADE)
   display=models.CharField(max_length=200)
   processor=models.CharField(max_length=200)
   memory=models.CharField(max_length=100)
   camera=models.CharField(max_length=100)
   battery=models.CharField(max_length=100)
   price=models.IntegerField()

   

       



   
