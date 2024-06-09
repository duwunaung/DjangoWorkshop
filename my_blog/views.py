from django.shortcuts import render, HttpResponse
from .models import About

def home_page(request):
    return render(request, "index.html", {'feature': range(2), 'recent': range(5)})

def blogs_page(request):
    return render(request, "blogs.html", {'article': range(10)} )


def blog_detail_page(request):
    return render(request, "detail.html", )

def about_page(request):
    info = About.objects.get(pk = 1)
    print (info)
    return render(request, "about.html", {
        'info': info
    })

def contact_page(request):
    return render(request, "contact.html")
