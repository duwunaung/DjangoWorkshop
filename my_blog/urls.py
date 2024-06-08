from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("blogs/<slug:category>", views.blogs_page, name = "blogs"),
    path("blogs/post_id", views.blog_detail_page)
]
