from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Explorer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    street = models.CharField(max_length=100,blank=True, null=True)
    city = models.CharField(max_length=100,blank=True, null=True)
    state = models.CharField(max_length=100,blank=True, null=True)
    total_use = models.IntegerField(blank=True, null=True)

# Create your models here.
