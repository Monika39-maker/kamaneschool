from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('noticeboard', views.noticeboard, name="noticeboard"),
    path('student', views.student, name="student"),
    path('studentlogin', views.studentlogin, name="studentlogin"),
    path('vision', views.vision, name="vision"),
    path('curriculum', views.curriculum, name="curriculum"),
    path('schedule', views.schedule, name="schedule"),
    path('environment', views.environment, name="environment"),
    path('contact', views.contact, name="contact"),
    path('logout', views.logout, name="logout")
]