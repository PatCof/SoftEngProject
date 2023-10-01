from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomManager

# Create your models here.

class Teachers(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    department = models.CharField(max_length=255, default="")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomManager()

    def save(self, *args, **kwargs):
        # Set the password using set_password method
        if self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.department}"

