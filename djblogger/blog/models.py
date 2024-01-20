from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    options = (
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    author = models.ForeignKey(to=User,on_delete=models.CASCADE, related_name='Articles')
    status = models.CharField(max_length=15,choices=options,default='draft')
    date_created = models.DateTimeField(auto_now_add=True,editable=False)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self):
        return self.title