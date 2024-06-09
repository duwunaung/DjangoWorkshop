from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name = "home"),
    path("blogs", views.blogs_page, name = "blogs"),
    path("blog", views.blog_detail_page, name = "blog"),
    path("about", views.about_page, name = "about"),
    path("contact", views.contact_page, name = "contact")
]
