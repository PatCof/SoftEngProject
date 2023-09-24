from django import forms
from .models import Teachers


class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ['email', 'password']
