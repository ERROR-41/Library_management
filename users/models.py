from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

# Create your models here.




class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    membership_date = models.DateTimeField(auto_now_add=True)
    address = models.TextField(max_length=40, blank=True, null=True)
    phone_number = models.TextField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email