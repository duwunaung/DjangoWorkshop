from django.shortcuts import render, HttpResponse
from .models import About, Blog, Comment
from .forms import ContactForm, CommentForm

def home_page(request):
    featured_blogs = Blog.objects.filter(is_featured = True, status="active")
    recent_blogs = Blog.objects.filter(status="active")
    return render(request, "index.html", 
    {'featured_blogs': featured_blogs, 'recent_blogs': recent_blogs[:5]}
    )

def blogs_page(request):
    blogs = Blog.objects.filter(status="active")
    return render(request, "blogs.html", {'articles': blogs} )


def blog_detail_page(request, slug):
    blog = Blog.objects.get(status="active", slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.blog = blog
            comment.save()
    comments = Comment.objects.filter(blog = blog)
    return render(request, "detail.html", {
        "form": CommentForm,
        "blog" : blog,
        "comments" : comments
    })

def about_page(request):
    info = About.objects.get(pk = 1)
    print (info)
    return render(request, "about.html", {
        'info': info
    })

def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return render(request, "contact.html", {
                "sent_message" : True
            })

    return render(request, "contact.html", {
        "form": ContactForm,
        "sent_message": False
    })
