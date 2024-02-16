from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.http import Http404

# Create your views here.
def index (request):
    return render(request,'index.html')

def register(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            # Create a new user
            newuser = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            # Create an associated EmployeeDetail using the newly created user
            EmployeeDetail.objects.create(user = newuser, empcode=ec)

            error="no"
        except:
            error ="yes"

    return render(request, 'register.html', locals())

def emp_login (request):
    error=""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request,'emp_login.html', locals())

def emp_home(request):
    # open only when user is logged in.
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request,'emp_home.html')

def signout(request):
    logout(request)
    # destroy the session and erdirect to index
    return redirect('index')

def profile(request):
    # open only when user is logged in.
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user
    try:
        employee = EmployeeDetail.objects.get(user=user)
    except EmployeeDetail.DoesNotExist:
        # Handle the case where the EmployeeDetail does not exist
        raise Http404("EmployeeDetail does not exist for this user.")

    # def explaination:
        # EmployeeDetail.objects.get - to get current user detals
        # EmployeeDetail.objects.all.get - to get all user detils
        # EmployeeDetail.objects.filter.get - to filter indivisual user detail

    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        desig = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        # .update data in profile in employee detail
        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode =ec
        employee.empdept = dept
        employee.designation = desig
        employee.contact = contact
        employee.gender = gender

        if jdate: 
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
            error= "no"
        except:
            error ="yes"

    return render(request, 'profile.html', locals())

def admin_login(request):
    error=""
    if request.method == 'POST':
        user = request.POST['username']
        passw = request.POST['pwd']
        user = authenticate(username=user,password=passw)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error="yes"
    return render(request,'admin_login.html', locals())

def admin_home(request):
    # open only when user is logged in.
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')

def my_experience(request):
    # open only when user is logged in.
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user
    try:
        # 
        experience = EmployeeExperience.objects.get(user=user)
    except EmployeeExperience.DoesNotExist:
        # Handle the case where the EmployeeDetail does not exist
        raise Http404("Employee Experience does not exist for this user.")
    return render(request, 'my_experience.html', locals())

def edit_experience(request):

    # open only when user is logged in.
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user
    try:
        experience = EmployeeExperience.objects.get(user=user)
    except EmployeeDetail.DoesNotExist:
        # Handle the case where the EmployeeDetail does not exist
        raise Http404("EmployeeExperience does not exist for this user.")

    if request.method == "POST":
        c1n = request.POST['c1name']
        c1d = request.POST['c1designation']
        c1s = request.POST['c1salary']
        c1du = request.POST['c1duration']

        c2n = request.POST['c2name']
        c2d = request.POST['c2designation']
        c2s = request.POST['c2salary']
        c2du = request.POST['c2duration']

        c3n = request.POST['c3name']
        c3d = request.POST['c3designation']
        c3s = request.POST['c3salary']
        c3du = request.POST['c3duration']

        # .update data in profile in employee detail
        experience.c1name = c1n
        experience.c1designation = c1d
        experience.c1salary = c1s
        experience.c1duration = c1du
        
        experience.c2name = c2n
        experience.c2designation = c2d
        experience.c2salary = c2s
        experience.c2duration = c2du

        experience.c3name = c3n
        experience.c3designation = c3d
        experience.c3salary = c3s
        experience.c3duration = c3du

        try:
            experience.save()
            # experience.user.save()
            error= "no"
        except:
            error ="yes"

    return render(request,'edit_experience.html', locals())

def my_education(request):
    # open only when user is logged in.
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user
    try:
        education = EmployeeEducation.objects.get(user=user)
    except EmployeeEducation.DoesNotExist:
        # Handle the case where the EmployeeDetail does not exist
        raise Http404("Employee Education does not exist for this user.")
    return render(request, 'my_education.html', locals())

def edit_myeducation(request):
    
    # open only when user is logged in.
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user
    try:
        education = EmployeeEducation.objects.get(user=user)
    except EmployeeDetail.DoesNotExist:
        # Handle the case where the EmployeeDetail does not exist
        raise Http404("EmployeeExperience does not exist for this user.")

    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassingpg = request.POST['yearofpassingpg']
        percentagepg = request.POST['percentagepg']

        courseug = request.POST['courseug']
        schoolclgug = request.POST['schoolclgug']
        yearofpassingug = request.POST['yearofpassingug']
        percentageug = request.POST['percentageug']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']

        # .update data in profile in employee detail
        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg
        
        education.courseug = courseug
        education.schoolclgug = schoolclgug
        education.yearofpassingug = yearofpassingug
        education.percentageug = percentageug

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        try:
            education.save()
            # experience.user.save()
            error= "no"
        except:
            error ="yes"

    return render(request,'edit_myeducation.html', locals())

def change_password(request):
    # open only when user is logged in.
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    error = ""
    user = request.user

    if request.method == "POST":
        curpass = request.POST['currentpassword']
        newpass = request.POST['newpassword']
        # cnfp =request.POST['confirmnewpassword']
        try:
            if user.check_password(curpass):
                # if password match the db
                user.set_password(newpass)
                user.save()
                error = "no"     
            else:
                error = "not"
                # pass doesnot match the database
        except:
            error = "yes"
        
        # try:
        #     # checking for password match
        #     if newpass != cnfp or newpass == curpass:
        #         error = "password does not match"
        #     else:
        #         # if current password match the psw in database
        #         if user.check_password(curpass):
        #             # pass is set new to the n varible
        #             user.set_password(newpass)
        #             user.save()
        #             error = "no"
        #         else:
        #             error = "wrong current password"
        # except:
        #     error = "yes"

    return render(request, 'change_password.html', locals())

def change_passwordadmin(request):
    # open only when user is logged in.
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    error = ""
    user = request.user

    if request.method == "POST":
        curpass = request.POST['currentpassword']
        newpass = request.POST['newpassword']
        # cnfp =request.POST['confirmnewpassword']
        try:
            if user.check_password(curpass):
                # if password match the db
                user.set_password(newpass)
                user.save()
                error = "no"     
            else:
                error = "not"
                # pass doesnot match the database
        except:
            error = "yes"
        
        # try:
        #     # checking for password match
        #     if newpass != cnfp or newpass == curpass:
        #         error = "password does not match"
        #     else:
        #         # if current password match the psw in database
        #         if user.check_password(curpass):
        #             # pass is set new to the n varible
        #             user.set_password(newpass)
        #             user.save()
        #             error = "no"
        #         else:
        #             error = "wrong current password"
        # except:
        #     error = "yes"

    return render(request, 'change_passwordadmin.html', locals())

def all_employee(request):
    # open only when user is logged in.
    if not request.user.is_authenticated:
        return redirect('admin_login')

    employee = EmployeeDetail.objects.all()

    return render(request, 'all_employee.html', locals())