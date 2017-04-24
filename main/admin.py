from tokenize import Comment

from django.contrib import admin

# Register your models here.
from main.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)