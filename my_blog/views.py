from django.shortcuts import render, HttpResponse

def home_page(request):
    return render(request, "index.html", {'feature': range(2), 'recent': range(5)})

def blogs_page(request):
    return render(request, "blogs.html", {'article': range(10)} )


def blog_detail_page(request):
    return render(request, "detail.html", )

def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    return render(request, "contact.html")
