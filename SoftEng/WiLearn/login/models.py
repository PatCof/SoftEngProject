from django.db import models

# Create your models here.


class Teachers(models.Model):
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)


