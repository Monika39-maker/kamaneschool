from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils import timezone

# Create your models here.


class Grade(models.Model):
    grade = models.CharField(max_length=10)

    def __str__(self):
        return str(self.grade)


class Remarks(models.Model):
    remark = models.CharField(max_length=6)

    def __str__(self):
        return str(self.remark)


class Term(models.Model):
    term = models.CharField(max_length=10)

    def __str__(self):
        return str(self.term)


class Schedule(models.Model):
    heading = models.CharField(max_length=50)
    paragraph1 = models.CharField(max_length=150, null=True, blank=True)
    paragraph2 = models.CharField(max_length=150, null=True, blank=True)
    paragraph3 = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return str(self.heading)


class StudentLogin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    transaction_complete = models.BooleanField(default=True)
    # grade_one = models.BooleanField(default=True)
    # grade_two = models.BooleanField(default=True)
    # grade_three = models.BooleanField(default=True)
    # grade_four = models.BooleanField(default=True)
    # grade_five = models.BooleanField(default=True)
    # grade_nine = models.BooleanField(default=True)
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, null=True, blank=True)
    term = models.ForeignKey(Term, on_delete=models.CASCADE, max_length=10)
    date_added = models.DateField()
    image = models.ImageField(null=True, blank=True)
    remarks = models.ForeignKey(
        Remarks, on_delete=models.CASCADE, max_length=20)
    teachers_message = models.CharField(max_length=200)
    # cognitive_skills = models.CharField(null=True, blank=True, max_length=5)
    # english = models.CharField(null=True, blank=True, max_length=5)
    # science = models.CharField(null=True, blank=True, max_length=5)
    # opt_math = models.CharField(null=True, blank=True, max_length=5)

    def __str__(self):
        return str(self.user.username)

# class Vacancy(models.Model):
#     image = models.ImageField(null=True, blank=True)


class Notice(models.Model):
    title = models.CharField(max_length=100)
    to = models.CharField(max_length=50)
    detail = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)
