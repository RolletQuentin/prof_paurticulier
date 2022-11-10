from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction

from django import forms

from authentication.models import Student, Teacher, SchoolSubject, School, Grade


class UserForm(UserCreationForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
        )
        help_text = {
            "username": None,
            "password1": None,
            "password2": None,
            "email": None,
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ("profile_picture", "interests", "grades")


class StudentForm(forms.ModelForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=SchoolSubject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    grade = forms.ModelChoiceField(queryset=Grade.objects.all(), required=True)
    school = forms.ModelChoiceField(queryset=School.objects.all(), required=True)

    class Meta:
        model = Student
        fields = ("interests", "school", "grade")


# Login Forms
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d’utilisateur")
    password = forms.CharField(
        max_length=63, widget=forms.PasswordInput, label="Mot de passe"
    )
