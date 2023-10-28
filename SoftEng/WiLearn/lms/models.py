from django.conf import settings
from django.db import models
from django_quill.fields import QuillField


# Create your models here.
class Announcements(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = QuillField()


class Courses(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_id = models.CharField(unique=True,max_length=255)
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    enrollment_start = models.DateField()
    enrollment_end = models.DateField()
    course_start = models.DateField()
    course_end = models.DateField()
    lab_time = models.CharField(max_length=255)
    lab_day = models.CharField(max_length=255)
    lecture_time = models.CharField(max_length=255)
    lecture_day = models.CharField(max_length=255)