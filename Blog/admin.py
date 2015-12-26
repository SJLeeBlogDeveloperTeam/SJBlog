from django.contrib import admin
from Blog.models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
# Register your models here.
admin.site.register(Article)
