from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'description', 'avatr']


admin.site.register(UserProfile, UserProfileAdmin)



class ArticleAdmin(admin.ModelAdmin):
	search_field = ['title', 'context']
	list_display = ['title', 'category', 'created_at']


admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'cover']



admin.site.register(Category, CategoryAdmin)