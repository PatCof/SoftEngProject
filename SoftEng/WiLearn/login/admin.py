from django.contrib import admin
from .models import Teachers
# Register your models here.

@admin.register(Teachers)
class UserAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Teachers)

@admin.register(Teachers)
class UserAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Teachers)