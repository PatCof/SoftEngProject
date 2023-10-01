from django.shortcuts import render, redirect
from .forms import TeacherModelForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Teachers
from .backends import CustomEmailBackend
from django.contrib.auth.hashers import make_password
from django.urls import reverse
# Create your views here.


def main(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = CustomEmailBackend().authenticate(request, username=email, password=password)
        print(f"HELLO: {user}")
        if user is not None:
            login(request, user=user, backend='login.backends.CustomEmailBackend')
            return render(request, 'register.html')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = TeacherModelForm(request.POST)
        if form.is_valid():
            email = form['email'].value()
            password = form['password'].value()
            print(Teachers.objects.filter(email=email))
            if not Teachers.objects.filter(email=email).exists():
                hashed = make_password(password)
                user = User.objects.create(email=email, password=hashed)
                user.save()
                form.save()
                return redirect(login_user)
        else:
            print(form.errors)
        return render(request, 'register.html', {'error_message': form.errors}) #CONCERN: HINDI SPECIFIED ANO TALAGA ISSUE OTHER THAN EMAIL NAKASULAT (DAPAT SPECIFIC)
    return render(request, 'register.html')


def logout_user(request):
    logout(request)
    return redirect(login_user)


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = CustomEmailBackend().authenticate(request, username=email, password=password)
        print(f"HELLO: {user}")
        if user is not None:
            login(request, user=user, backend='login.backends.CustomEmailBackend')
            return render(request, 'register.html')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    else:
        return render(request, 'registration/login.html')

    #     form = TeacherModelForm(data=request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']
    #         user = CustomEmailBackend().authenticate(request, username=email, password=password)
    #         print(f"HELLO: {user}")
    #         if user is not None:
    #             login(request, user=user)
    #             return render(request, 'register.html')
    #         else:
    #             messages.error(request, 'Invalid login credentials. Please try again.')
    #     else:
    #         print(form.data)
    #         print(form.errors)
    #         messages.error(request, 'ERROR IS HERE')
    #         return redirect('login')
    #
    # else:
    #     form = TeacherModelForm()
    #     return render(request, 'registration/login.html', {'form': form})








# def login_user(request):
#     if request.method == 'POST':
#         form = TeacherModelForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             backend = CustomEmailBackend()
#             user = backend.authenticate(request, username=email, password=password)
#             print(f"{email} || {password}")
#             print(user)
#             if user is not None:
#                 login(request, user)
#                 return render(request, 'register.html')
#             else:
#                 return render(request, 'login.html')
#                 # return redirect('dashboard')
#     return render(request, 'login.html')

