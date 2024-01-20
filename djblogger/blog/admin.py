from django.contrib import admin
from . import models as blog
# Register your models here.
admin.site.register(blog.Article)
