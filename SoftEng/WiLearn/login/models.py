from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Teachers(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    department = models.CharField(max_length=255, default="")

    REQUIRED_FIELDS = ['email']



## PROBLEM IS THIS ONE: TRYING TO FIND SOLUTIONS
    #CONCERN: EACH TIME BUBUKSAN SA DJANGO ADMIN ANG ISANG USER, BAGONG HASH NG PASSWORD MANGYAYARI

    ##If ganto format, once lang siya ihash since passwords are less than 20
    def save(self, *args, **kwargs):
        if len(self.password) <= 20:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_full_name()} || {self.department}"
