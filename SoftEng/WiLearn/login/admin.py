from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Teachers
# Register your models here.


class TeachersAdmin(UserAdmin):
    ordering = ('username', 'first_name', 'last_name', 'email', 'password')
    list_display = ['first_name', 'last_name', 'username', 'email']
    fieldsets = (
        ("Teacher's Information", {'fields': ('first_name', 'last_name', 'username', 'email', 'password',)}),
         )

    # add_fieldsets = (
    #     ("Teacher's Information", {'fields': ('first_name', 'last_name', 'email', 'password','username')}),
    # )
    #
    # def add_view(self, request, form_url='', extra_context=None):
    #     self.fieldsets = self.add_fieldsets
    #     return super().add_view(request, form_url, extra_context)


admin.site.register(Teachers, TeachersAdmin)
