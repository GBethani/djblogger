from django.contrib import admin
from . import models as blog
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['short_title','tag_list',]

    def short_title(self,obj):
        max_length = 30
        new_title = obj.title[:30] + '......'
        return new_title if len(obj.title) > max_length else obj.title
    
    short_title.short_description = "Title"

    def tag_list(self,obj):
        return u", ".join(o.name for o in obj.tags.all())

admin.site.register(blog.Article,ArticleAdmin)
