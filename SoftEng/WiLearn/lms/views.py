from django.shortcuts import render, redirect
from .forms import AnnouncementForm, CourseForm
from .models import Announcements, Courses
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from random import randint
from PIL import Image

# Create your views here.
User = get_user_model()
COMPARISON_DICT = {10: "00000", 100: "0000", 1000: "000", 10000: "00", 100000: "0"}


@login_required
def dashboard(request):
    print(request.user.is_authenticated)
    user = request.user
    print(user.id)
    course = Courses.objects.filter(user_id=user.id)
    announcement = Announcements.objects.filter(user_id=user.id)

    return render(request, 'lms/dashboard.html', {'course': course, 'announcement': announcement})


@login_required
def inbox(request):
    return render(request, 'lms/inbox.html')


@login_required
def post_announcements(request):
    if request.method == 'POST':
        announcement_form = AnnouncementForm(request.POST)
        if announcement_form.is_valid():
            user = request.user
            teacher = User.objects.get(email=user.email)
            announcement = announcement_form.save(commit=False)

            title = announcement_form.cleaned_data['title']
            # text = announcement_form.cleaned_data['text']
            announcement.title = title
            announcement.user = teacher
            announcement.save()
            return redirect('lms:dashboard')
        else:
            print(announcement_form)
            print(announcement_form.errors)

    form = AnnouncementForm()
    return render(request, 'lms/postannouncement.html', {'form': form})


@login_required
def add_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)
        print("HEELO")
        if course_form.is_valid():
            user = request.user
            teacher = User.objects.get(email=user.email)
            if teacher is not None:
                last = Courses.objects.all().last()
                last.id += 1
                course = course_form.save(commit=False)
                course.user = teacher
                for key,val in COMPARISON_DICT.items():
                    if last.id < key:
                        course.course_id = f"{teacher.last_name}.{val}{last.id}"
                        break
                    elif last.id >= 100000:
                        course.course_id = f"{teacher.last_name}.{last.id}"
                        break
                course.save()

            return redirect('lms:dashboard')
        else:
            print(course_form)
            print(course_form.errors)

    form = CourseForm()
    return render(request, 'lms/addcourse.html', {'form': form})




# TODO#2: FIX ADMIN-SIDE CREATE USER (ADD EMAIL FIELD)