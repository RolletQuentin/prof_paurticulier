from django.shortcuts import render

from blog.models import Ticket

def blog_view(request):
    blogs = Ticket.objects.all()
    return render(request, "blog/blog.html", {'blogs': blogs})


def blog_details_view(request, id):
    blog = Ticket.objects.get(id=id)
    return render(request, "blog/blog_detail.html", {'blog': blog})
