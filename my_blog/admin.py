from django.contrib import admin
from .models import Author, Blog, About, Contact

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'email', 'createddate')

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status")

class ContactAdmin(admin.ModelAdmin):
    list_filter = ("status", )
    list_display = ("name", "email", "createddate", "status")

admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(About)
admin.site.register(Contact, ContactAdmin)