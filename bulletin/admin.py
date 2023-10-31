from django.contrib import admin

from bulletin.models import Like, Post, Comment

admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Post)

