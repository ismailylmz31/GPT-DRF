from django.contrib import admin
from .models import Author, Book
from django.contrib.auth.models import Group, User

admin.site.register(Author)
admin.site.register(Book)
