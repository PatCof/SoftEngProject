from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.register),
  path('login_user/', views.login_user, name="login"),
  path('logout/', views.logout_user),
  path('', views.main, name='main'),
]
