from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# How to implement multiple user types : https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html


class User(AbstractUser):
    phone = PhoneNumberField(blank=True)
    is_student = models.BooleanField("student status", default=False)
    is_teacher = models.BooleanField("teacher status", default=False)

    def __str__(self):
        return str(self.username)


class School(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)


class SchoolSubject(models.Model):
    name = models.CharField(max_length=30, unique=True, primary_key=True)


class Grade(models.Model):

    name = models.CharField(
        max_length=30,
        verbose_name="Niveau",
        unique=True,
        primary_key=True,
    )


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_picture = models.ImageField(upload_to="static/images/")
    interests = models.ManyToManyField(SchoolSubject, blank=True)
    grades = models.ManyToManyField(Grade, blank=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    interests = models.ManyToManyField(SchoolSubject, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
