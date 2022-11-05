from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View, CreateView

# from django import forms
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
class StudentsSignUpView(CreateView):
    template_name = "authentication/student_signup.html"
    model = models.User
    form_class = forms.StudentsSignUpForm

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "student"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class TeachersSignUpView(CreateView):
    template_name = "authentication/teacher_signup.html"
    model = models.User
    form_class = forms.TeachersSignUpForm

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "student"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


# Update informations
@login_required
def update_user(request):
    user = models.User.objects.get(username=request.user.username)
    if user.is_teacher:
        form = forms.TeachersSignUpForm(instance=user)
    elif user.is_student:
        form = forms.StudentsSignUpForm(instance=user)
    else:
        form = forms.SignUpForm(instance=user)
    return render(request, "authentication/update_user.html", {"form": form})


# Log out
def logout_user(request):
    logout(request)
    return redirect("login")


# Bullshit
def home(request):
    return render(request, "authentication/home.html")


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
