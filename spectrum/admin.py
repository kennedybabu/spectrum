from django.contrib import admin
from .models import Interest, Post, Comment
# Register your models here.

admin.site.register(Interest)
admin.site.register(Comment)
admin.site.register(Post)