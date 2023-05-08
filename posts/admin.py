from django.contrib import admin
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'published']

admin.site.register(Post, PostAdmin)