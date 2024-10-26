from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Contact(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'user'