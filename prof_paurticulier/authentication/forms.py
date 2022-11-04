from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from django import forms

from authentication.models import Student, Teacher, User, SchoolSubject, School, Grade


class StudentsSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=SchoolSubject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    grade = forms.ModelChoiceField(queryset=Grade.objects.all(), required=True)
    school = forms.ModelChoiceField(queryset=School.objects.all(), required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.interest.add(*self.cleaned_data.get("interests"))
        student.grade.add(*self.cleaned_data.get("grade"))
        student.school.add(*self.cleaned_data.get("school"))
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d’utilisateur")
    password = forms.CharField(
        max_length=63, widget=forms.PasswordInput, label="Mot de passe"
    )
