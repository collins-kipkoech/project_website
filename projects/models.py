from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']
