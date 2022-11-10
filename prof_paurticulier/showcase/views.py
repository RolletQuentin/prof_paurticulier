from django.shortcuts import render
from django.core.paginator import Paginator

from authentication.models import Teacher


def home(request):
    return render(request, "showcase/home.html")


def showcase(request):
    teachers = Teacher.objects.all()

    paginator = Paginator(teachers, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "showcase/showcase.html", context={"page_obj": page_obj})
