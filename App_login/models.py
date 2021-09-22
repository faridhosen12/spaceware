from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    User = models.OneToOneField(User, related_name='user_profile',on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to ='profile_pics')
