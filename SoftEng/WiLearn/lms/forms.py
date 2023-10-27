from django import forms
from .models import Announcements, Courses
from django_quill.forms import QuillFormField


class AnnouncementForm(forms.ModelForm):
    title = forms.CharField()
    text = QuillFormField()

    class Meta:
        model = Announcements
        fields = ['title', 'text']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('img',
                  'name',
                  'desc',
                  'enrollment_start',
                  'enrollment_end',
                  'course_start',
                  'course_end',
                  'lab_time',
                  'lab_day',
                  'lecture_time',
                  'lecture_day',)
        exclude = ['user']
        labels = {
            "img": "Course Image",
            "name": "Course Name",
            "desc": "Course Description",
            "enrollment_start": "Enrollment Start Date",
            "enrollment_end": "Enrollment End Date",
            "course_start": "Course Start Date",
            "course_end": "Course End Date",
            "lab_time": "Laboratory Time",
            "lab_day": "Laboratory Day",
            "lecture_time": "Lecture Time",
            "lecture_day": "Lecture Day",
        }

        widgets = {
            "img": forms.FileInput(attrs={'id': "courseImage"}),
            "name": forms.TextInput(attrs={'id': "courseName"}),
            "desc": forms.Textarea(attrs={'id': "courseDescription"}),
            "enrollment_start": forms.SelectDateWidget(attrs={'id': "enrollmentStartDate"}),
            "enrollment_end": forms.SelectDateWidget(attrs={'id': "enrollmentEndDate"}),
            "course_start": forms.SelectDateWidget(attrs={'id': "courseStartDate"}),
            "course_end": forms.SelectDateWidget(attrs={'id': "courseEndDate"}),
            "lab_time": forms.TextInput(attrs={'id': "labTime"}),
            "lab_day": forms.TextInput(attrs={'id': "labDay"}),
            "lecture_time": forms.TextInput(attrs={'id': "lectureTime"}),
            "lecture_day": forms.TextInput(attrs={'id': "lectureDay"}),
        }

