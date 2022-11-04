from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View, CreateView

# from django import forms
from . import models, forms


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


def home(request):
    return render(request, "authentication/home.html")
