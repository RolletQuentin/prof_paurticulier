from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.db.models.signals import post_save

# How to implement multiple user types : https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html


class User(AbstractUser):
    phone = PhoneNumberField(blank=True)
    is_student = models.BooleanField("student status", default=False)
    is_teacher = models.BooleanField("teacher status", default=False)

    def __str__(self):
        return str(self.username)


class School(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
        return str(self.name)


class SchoolSubject(models.Model):
    name = models.CharField(max_length=30, unique=True, primary_key=True)

    def __str__(self):
        return str(self.name)


class Grade(models.Model):

    name = models.CharField(
        max_length=30,
        verbose_name="Niveau",
        unique=True,
        primary_key=True,
    )

    def __str__(self):
        return str(self.name)


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name="teacher_profile"
    )
    profile_picture = models.ImageField(
        upload_to="static/images/", blank=True, null=True
    )
    interests = models.ManyToManyField(SchoolSubject, blank=True)
    grades = models.ManyToManyField(Grade, blank=True)

    def __str__(self):
        return str(self.user)


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name="student_profile"
    )
    interests = models.ManyToManyField(SchoolSubject, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, **kwargs):
#     # print("****", created)
#     if instance.is_teacher:
#         Teacher.objects.get_or_create(user=instance)
#     else:
#         Student.objects.get_or_create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.is_teacher:
#         instance.teacher_profile.save()
#     else:
#         instance.student_profile.save()
