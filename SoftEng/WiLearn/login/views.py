from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .backends import CustomEmailBackend
from django.urls import reverse
# Create your views here.


def main(request):
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

    return render(request, 'index.html')


def logout_user(request):
    logout(request)
    return redirect(main)


# def login_user(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = CustomEmailBackend().authenticate(request, username=email, password=password)
#         print(f"HELLO: {user}")
#         if user is not None:
#             login(request, user=user, backend='login.backends.CustomEmailBackend')
#             # return render(request, 'register.html')
#             admin_url = reverse('admin:index')
#             return render(request, admin_url)
#         else:
#             messages.error(request, 'Invalid login credentials. Please try again.')
#
#     else:
#         return render(request, 'registration/login.html')
#
#







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