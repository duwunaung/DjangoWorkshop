from django.contrib import admin
from .models import Author, Blog, About

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'email', 'createddate')

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status")

admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(About)