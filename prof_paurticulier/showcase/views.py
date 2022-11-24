from django.shortcuts import render
from django.core.paginator import Paginator

from authentication.models import Teacher
from . import forms


def home(request):
    return render(request, "showcase/home.html")


def showcase(request):
    # TODO : https://stackoverflow.com/questions/71443933/paginator-and-post-request-for-searchform
    def teachers_filter(teachers, interests, grades):
        teachers_filter_list_interests = []
        teachers_filter_list = []
        if len(interests) == 0:
            teachers_filter_list_interests = teachers
        else:
            for teacher in teachers:
                for interest in interests:
                    if interest in teacher.interests.all():
                        teachers_filter_list_interests.append(teacher)
        if len(grades) == 0:
            teachers_filter_list = teachers_filter_list_interests
        else:
            for teacher in teachers_filter_list_interests:
                for grade in grades:
                    if grade in teacher.grades.all():
                        teachers_filter_list.append(teacher)
        return list(set(teachers_filter_list))

    teachers = Teacher.objects.all()

    if request.method == "POST":
        filter_form = forms.FilterShowcaseForm(request.POST, prefix="FF")

        if filter_form.is_valid():
            interests = filter_form.cleaned_data.get("interests")
            grades = filter_form.cleaned_data.get("grades")
            teachers = teachers_filter(teachers, interests, grades)

    else:
        filter_form = forms.FilterShowcaseForm(prefix="FF")

    paginator = Paginator(teachers, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "showcase/showcase.html",
        context={
            "page_obj": page_obj,
            "filter_form": filter_form,
            "teachers": teachers,
        },
    )


def teacher_view(request, id):
    teacher = Teacher.objects.get(id=id)
    return render(request, "showcase/teacher_detail.html", {"teacher": teacher})
