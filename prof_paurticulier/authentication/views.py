from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View, CreateView

from . import models, forms


# Log In
class LoginPageView(View):
    template_name = "authentication/login.html"
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("home")
        message = "Identifiants invalides."
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )


# Sign Up
def signup(request):
    return render(request, "authentication/signup.html")


def teacher_signup_view(request):

    if request.method == "POST":
        user_form = forms.UserForm(request.POST, prefix="UF")
        profile_form = forms.TeacherForm(request.POST, request.FILES, prefix="PF")

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_teacher = True
            user.save()

            teacher = profile_form.save(commit=False)
            teacher.user = models.User.objects.get(pk=user.id)
            teacher.profile_picture = profile_form.cleaned_data.get("profile_picture")
            teacher.save()
            teacher.interests.set(profile_form.cleaned_data.get("interests"))
            teacher.grades.set(profile_form.cleaned_data.get("grades"))

            login(request, user)
            return redirect("home")

    else:
        user_form = forms.UserForm(prefix="UF")
        profile_form = forms.TeacherForm(prefix="PF")

    return render(
        request,
        "authentication/teacher_signup.html",
        {"user_form": user_form, "teacher_profile_form": profile_form},
    )


def student_signup_view(request):

    if request.method == "POST":
        user_form = forms.UserForm(request.POST, prefix="UF")
        profile_form = forms.StudentForm(request.POST, prefix="PF")

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_student = True
            user.save()

            student = profile_form.save(commit=False)
            student.user = models.User.objects.get(pk=user.id)
            student.save()
            student.interests.set(profile_form.cleaned_data.get("interests"))

            login(request, user)
            return redirect("home")

    else:
        user_form = forms.UserForm(prefix="UF")
        profile_form = forms.StudentForm(prefix="PF")

    return render(
        request,
        "authentication/student_signup.html",
        {"user_form": user_form, "student_profile_form": profile_form},
    )


# Update informations
@login_required
def update_user(request):
    user = models.User.objects.get(username=request.user.username)
    if user.is_teacher:
        teacher = models.Teacher.objects.get(user_id=request.user.id)
        user_form = forms.UserForm(instance=user)
        profile_form = forms.TeacherForm(instance=teacher)
    elif user.is_student:
        student = models.Student.objects.get(user_id=request.user.id)
        user_form = forms.UserForm(instance=user)
        profile_form = forms.StudentForm(instance=student)
    return render(
        request,
        "authentication/update_user.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


# Log out
def logout_user(request):
    logout(request)
    return redirect("home")


# Bullshit


def set_initial_dataset(request):
    # Grades
    models.Grade(name="6ème").save()
    models.Grade(name="5ème").save()
    models.Grade(name="4ème").save()
    models.Grade(name="3ème").save()
    models.Grade(name="2nd").save()
    models.Grade(name="1ère").save()
    models.Grade(name="Term.").save()
    models.Grade(name="Prépa").save()

    # SchoolSubject
    models.SchoolSubject(name="Maths").save()
    models.SchoolSubject(name="Physique").save()
    models.SchoolSubject(name="Chimie").save()
    models.SchoolSubject(name="Français").save()
    models.SchoolSubject(name="Anglais").save()
    models.SchoolSubject(name="Informatique").save()

    # School
    models.School(name="Lycée A").save()
    models.School(name="Lycée B").save()
    models.School(name="Lycée C").save()
    models.School(name="Collège A").save()
    models.School(name="Collège A").save()
    return redirect("home")
