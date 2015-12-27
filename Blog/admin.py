from django.contrib import admin
from Blog.models import Article
from bootstrap_admin import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
# Register your models here.
admin.site.register(Article)
