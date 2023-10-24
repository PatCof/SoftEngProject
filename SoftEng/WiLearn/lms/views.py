from django.shortcuts import render, redirect
from .forms import AnnouncementForm, CourseForm
from .models import Announcements, Courses
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from random import randint
from PIL import Image

# Create your views here.
User = get_user_model()

@login_required
def dashboard(request):
    print(request.user.is_authenticated)
    user = request.user
    print(user.id)
    course = Courses.objects.filter(user_id=user.id)
    return render(request, 'lms/dashboard.html', {'course': course})


@login_required
def inbox(request):
    return render(request, 'lms/inbox.html')


@login_required
def post_announcements(request):
    if request.method == 'POST':
        announcement_form = AnnouncementForm(request.POST)
        if announcement_form.is_valid():
            title = announcement_form.cleaned_data['Announcement_Title']
            text = announcement_form.cleaned_data['Announcement_Content']
            print(f"{title} + {text}")
            a = Announcements(title=title, text=text)
            a.save()
            return redirect('dashboard')
        else:
            print(announcement_form)
            print(announcement_form.errors)

    form = AnnouncementForm()
    return render(request, 'lms/postannouncement.html', {'form': form})

    # return render(request, 'lms/postannouncement.html', {'form': form})


@login_required
def add_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)
        print("HEELO")
        if course_form.is_valid():
            user = request.user
            teacher = User.objects.get(email=user.email)
            if teacher is not None:
                course = course_form.save(commit=False)
                course.user = teacher
                c_id = generate_course_id()
                course.course_id = c_id
                course.save()

            return redirect('lms:dashboard')
        else:
            print(course_form)
            print(course_form.errors)

    form = CourseForm()
    return render(request, 'lms/addcourse.html', {'form': form})

# def generate_course_id():
#     random_id = randint(10000, 99999)
#     print(random_id)
#     flag = True
#     if Courses.objects.filter(course_id= random_id):


#
def generate_course_id():
    random_id = randint(10000, 99999)
    print(random_id)
    print(Courses.objects.filter(course_id=random_id))
    # TODO# 1 FIX LOOP FOR RANDOM COURSE_ID TO PREVENT DUPLICATE VALUES
    if not Courses.objects.filter(course_id=random_id):
        random_id = randint(10000, 99999)
        

    # if not Courses.objects.filter(course_id=random_id):
    #     while True:
    #         random_id = randint(10000, 99999)
    #         print(random_id)
    #         if Courses.objects.filter(course_id=random_id):
    #             break
    return random_id


# TODO#2: FIX ADMIN-SIDE CREATE USER (ADD EMAIL FIELD)