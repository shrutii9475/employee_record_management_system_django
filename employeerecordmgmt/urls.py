"""
URL configuration for employeerecordmgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('register/',register,name='register'),
    path('emp_login/',emp_login,name='emp_login'),
    path('emp_home/',emp_home,name='emp_home'),
    path('profile/',profile, name='profile'),    
    path('signout/',signout, name='signout'),
    path('admin_login/',admin_login, name='admin_login'),
    path('my_experience/',my_experience, name='my_experience'),
    path('edit_experience/',edit_experience, name='edit_experience'),
    path('my_education/',my_education, name='my_education'),
    path('edit_myeducation/',edit_myeducation, name='edit_myeducation'),
    path('change_password/',change_password, name='change_password'),
]
