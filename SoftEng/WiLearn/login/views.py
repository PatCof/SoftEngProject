from django.shortcuts import render, redirect
from .forms import TeacherModelForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import Teachers
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = TeacherModelForm(request.POST)
        if form.is_valid():
            email = form['email'].value()
            print(Teachers.objects.filter(email=email))
            if not Teachers.objects.filter(email=email).exists():
                form.save()
                return redirect(login_user)
        else:
            print(form.errors)
        return render(request, 'register.html', {'error_message': form.errors}) #CONCERN: HINDI SPECIFIED ANO TALAGA ISSUE OTHER THAN EMAIL NAKASULAT (DAPAT SPECIFIC)
    return render(request, 'register.html')


def login_user(request):
    # if request.method == "GET":
    #     form = TeacherModelForm(request.GET)
    #     if form.is_valid():
    #         user = authenticate(email=form['email'].value(), password=form['password'].value())
    #         if user:
    #             login(request, user)
    #             return HttpResponse(f"<h1>{user}<h1>")
    #        # if form.cleaned_data['email']
    return render(request, 'login.html')
