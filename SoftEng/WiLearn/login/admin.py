from django.contrib import admin
from .models import Teachers
# Register your models here.


class TeachersAdmin(admin.ModelAdmin):
    admin.site.register(Teachers)


