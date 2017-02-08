from django.template import Context, Template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# ---------------------------
# --  Method-Based Views   --
# ---------------------------
#  Index View
# @descr This is the splash page that all unauthorized users will get when visitng our base url.
# @TODO  Figure out what to put on this page (so far: FAQ, Feedback, UserManual links)
# @update 1/31/17
def IndexView(request):
    return render(request, 'index.html')

#  Home View
# @descr The view that logged in users will see and will contain their control panel.
#        Will have a different control panel based on the authenticated user.
# @TODO  Add control panel for scheduler first, then add mechanism for loading based on usertype,
#        then add control panel for faculty.
# @update 1/31/17
def HomeView(request):
    return render(request, 'home.html')

#  Rooms View
# @descr 
# @TODO 
# @update 2/2/17
def RoomsView(request):
    return render(request, 'rooms.html')

#  Courses View
# @descr 
# @TODO 
# @update 2/5/17
from .models import Course
from .forms import AddCourseForm
def CoursesView(request):
    res = HttpResponse()
    if request.method == "GET":
        #TODO should filter by those with usertype 'scheduler'
        return render(request, 'courses.html', {
                'course_list': Course.objects.filter(),
                'add_course_form':AddCourseForm()
            });
    elif request.method == "POST":
        form = AddCourseForm(request.POST); 
        if form.is_valid():
            form.addCourse();
            res.status_code = 200
    return render(request, 'courses.html')

#  Schedulers View
# @descr Displays all of the schedulers currecntly registered in the database.
#        Also includes a + and - button that link to the invite form and delete form
# @update 2/4/17
def SchedulersView(request):
    res = HttpResponse()
    if request.method == "GET":
        #TODO should filter by those with usertype 'scheduler'
        return render(request, 'schedulers.html', {
                'scheduler_list': User.objects.filter(), 
                'invite_user_form': InviteUserForm(),
                'delete_user_form': DeleteUserForm()
            });
    elif request.method == "POST" and 'invite-form' in request.POST:
        form = InviteUserForm(request.POST)
        if form.is_valid():
            form.send_invite('scheduler')
            res.status_code = 200
        else:
            res.status_code = 400
    elif request.method == "POST" and 'delete-form' in request.POST:
        form = DeleteUserForm(request.POST)
        if form.is_valid():
            print('NYI')
            res.status_code = 200
        else:
            res.status_code = 400
    else:
        res.status_code = 400
    return res

#  Faculty View
# @descr Display all of the faculty currently registered in the database.
#        Also includes a + and - button that link to theinvite form and delete form
# @update 2/2/17
from .models import User
from .forms import InviteUserForm, DeleteUserForm
def FacultyView(request):
    res = HttpResponse()
    if request.method == "GET":
        #TODO should filter by those with usertype 'faculty'
        return render(request, 'faculty.html', {
                'faculty_list': User.objects.filter(), 
                'invite_user_form': InviteUserForm(),
                'delete_user_form': DeleteUserForm()
            });
    elif request.method == "POST" and 'invite-form' in request.POST:
        form = InviteUserForm(request.POST)
        if form.is_valid():
            form.send_invite('faculty')
            res.status_code = 200
        else:
            res.status_code = 400
    elif request.method == "POST" and 'delete-form' in request.POST:
        form = DeleteUserForm(request.POST)
        if form.is_valid():
            print('NYI')
            res.status_code = 200
        else:
            res.status_code = 400
    else:
        res.status_code = 400
    return res


# ---------------------------
# --   Class-Based Views   --
# ---------------------------
# @NOTE:Use method-based views for now. They are simpler.

