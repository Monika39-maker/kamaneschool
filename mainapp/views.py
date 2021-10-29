from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *
from django.contrib.auth.models import User, auth
from django.utils.translation import gettext as _

# Create your views here.
from django.shortcuts import render

def index(request):
    context = {
        'hello': _('Hello')
    }
    return render(request, 'index.html', context)



def noticeboard(request):
    # vacancies = Vacancy.objects.all()
    notices = Notice.objects.all()
    # context = {'vacancies':vacancies, 'notices':notices}
    context = {'notices':notices}
    return render(request, 'noticeboard.html', context)

def studentlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(student)

        else:
            return render(request, 'studentlogin.html', {'error': "Invalid Login Credentials"})
    else:
        return render(request, 'studentlogin.html')


def student(request):
    log_user = request.user    
    results = StudentLogin.objects.filter(user=log_user)
    return render(request, 'student.html', {'results':results})
        
def logout(request):
    auth.logout(request)
    return redirect(index) 


def vision(request):
    return render(request, 'vision.html')

def curriculum(request):
    return render(request, 'curriculum.html')

def schedule(request):
    
    schedules = Schedule.objects.all()
    
    context = {'schedules':schedules}
    
    return render(request, 'schedule.html', context)

def environment(request):
    return render(request, 'environtment.html')
    
    
def contact(request):
    return render(request, 'contact.html')

