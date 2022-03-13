from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin (admin.ModelAdmin):
    list_display = ('title','tags','status','created_on')
    list_filter = ("status",)
    search_fields = ['title','content']
    prepopulated_fields = {'tags':('title',)}


admin.site.register(Post, PostAdmin)