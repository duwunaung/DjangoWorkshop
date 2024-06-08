from django.shortcuts import render, HttpResponse

def home_page(request):
    return render(request, "index.html")

def blogs_page(request, category):
    print(category)
    return render(request, "blogs.html", {
        'category': category
    })


def blog_detail_page(request):
    return HttpResponse("This is detail page")