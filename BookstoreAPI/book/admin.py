from django.contrib import admin
from .models import Author, Book
from django.contrib.auth.models import Group, User

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Group)
admin.site.register(User)

assistant_group, created = Group.objects.get_or_create(name='Assistant')

user = User.objects.get(username='assistant_user')
user.groups.add(assistant_group)
