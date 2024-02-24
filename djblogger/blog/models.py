from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Article(models.Model):
    options = (
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(to=User,on_delete=models.CASCADE, related_name='Articles')
    status = models.CharField(max_length=15,choices=options,default='draft')
    tags = TaggableManager()
    date_created = models.DateTimeField(auto_now_add=True,editable=False)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date_created",)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('article-detail',args=[self.slug])

    def __str__(self):
        return self.title