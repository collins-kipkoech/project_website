from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    image = models.ImageField(default='avatar.png',upload_to = 'profile_pictures')
    description = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.user.username

