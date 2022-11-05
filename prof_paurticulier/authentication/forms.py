from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from django import forms

from authentication.models import Student, Teacher, User, SchoolSubject, School, Grade


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        user = get_user_model()
        fields = ("username", "email", "first_name", "last_name")


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
        student = Student.objects.create(
            user=user,
            grade=self.cleaned_data.get("grade"),
            school=self.cleaned_data.get("school"),
        )
        student.interests.add(*self.cleaned_data.get("interests"))
        return user


class TeachersSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=SchoolSubject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    grades = forms.ModelMultipleChoiceField(
        queryset=Grade.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    profil_picture = forms.ImageField(required=False)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["profile_picture"].required = False

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(
            user=user,
            profile_picture=self.cleaned_data.get("profil_picture"),
        )
        teacher.interests.add(*self.cleaned_data.get("interests"))
        teacher.grades.add(*self.cleaned_data.get("grades"))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d’utilisateur")
    password = forms.CharField(
        max_length=63, widget=forms.PasswordInput, label="Mot de passe"
    )
