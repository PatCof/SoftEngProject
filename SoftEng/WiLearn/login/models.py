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

#Hello
## PROBLEM IS THIS ONE: TRYING TO FIND SOLUTIONS
    #CONCERN: EACH TIME BUBUKSAN SA DJANGO ADMIN ANG ISANG USER, BAGONG HASH NG PASSWORD MANGYAYARI
    # def save(self, *args, **kwargs):
    #     # Set the password using set_password method
    #     if not self.pk or self.password:
    #         self.set_password(self.password)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email} {self.password} | {self.department}"