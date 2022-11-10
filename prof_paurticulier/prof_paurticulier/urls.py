"""prof_paurticulier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from authentication.views import (
    LoginPageView,
    signup,
    student_signup_view,
    teacher_signup_view,
    update_user,
    logout_user,
    home,
    set_initial_dataset,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    # authentication
    path("login/", LoginPageView.as_view(), name="login"),
    path("signup", signup, name="signup"),
    path("signup/student/", student_signup_view, name="student_sign_up"),
    path("signup/teacher/", teacher_signup_view, name="teacher_sign_up"),
    path("user-change/", update_user, name="update_user"),
    path("logout/", logout_user, name="logout"),
    path("set-initial-dataset/", set_initial_dataset, name="set_initial_dataset"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
