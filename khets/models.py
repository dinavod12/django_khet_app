from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
   name=models.CharField(max_length=200)
   content=models.TextField()
   address=models.CharField(max_length=200)
   Date=models.DateTimeField(default=timezone.now)
   author=models.ForeignKey(User,on_delete=models.CASCADE)

   def __str__(self):
       return f'{self.name},{self.address}'

   def get_absolute_url(self):
       return reverse('blog-detail',kwargs={'pk':self.pk}) 