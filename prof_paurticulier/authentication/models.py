from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone = PhoneNumberField(blank=True)
    is_student = models.BooleanField("student status", default=False)
    is_teacher = models.BooleanField("teacher status", default=False)


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


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    interests = models.ManyToManyField(SchoolSubject)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
