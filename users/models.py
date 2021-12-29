from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pic')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        i=Image.open(self.image.path)
        if i.height>300 or i.width>300:
            outsize=(300,300)
            i.thumbnail(outsize)
            i.save(self.image.path)