from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .backends import EmailBackend
# Create your views here.


def main(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = EmailBackend().authenticate(request, username=email, password=password)
        print(f"HELLO: {user}")
        if user is not None:
            login(request, user=user, backend='login.backends.EmailBackend')
            return render(request, 'login/courses.html')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    return render(request, 'login/index.html')


def courses(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = EmailBackend().authenticate(request, username=email, password=password)
        print(f"HELLO: {user}")
        if user is not None:
            login(request, user=user, backend='login.backends.EmailBackend')
            return render(request, 'login/courses.html')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    return render(request, 'login/courses.html')


# def logout_user(request):
#     logout(request)
#     return redirect(main)

