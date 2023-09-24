from django.shortcuts import render, redirect
from .forms import TeacherModelForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = TeacherModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(login_user)
    return render(request, 'register.html')


def login_user(request):
    if request.method == "GET":
        form = TeacherModelForm(request.GET)
        if form.is_valid():
            user = authenticate(email=form["email"].value(), password=form['password'].value())
            if user:
                login(request, user)
                return HttpResponse(f"<>{user}<>")
           # if form.cleaned_data['email']
    return render(request, 'login.html')
