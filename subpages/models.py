from django.db import models
from django.contrib.auth.models import User
from homepage.models import Smartphone

# Create your models here.

class Comment(models.Model):
   STATUS=(
      ('New','New'),
      ('True','True'),
      ('False','False'),
   )
   smartphone=models.ForeignKey(Smartphone,on_delete=models.CASCADE)
   user=models.ForeignKey(User, on_delete=models.CASCADE)
   rate=models.IntegerField(default=1)
   comment=models.CharField(max_length=250, blank=True)
   status=models.CharField(max_length=10,choices=STATUS, default='New')
   created_at=models.DateTimeField(auto_now_add=True)
   updated_at=models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.user.username
       
