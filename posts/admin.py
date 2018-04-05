from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display= ['title', 'author', 'created']
	list_filter = ['author']
	search_fields = ['title']
	

admin.site.register(Post, PostAdmin)
