from django import template
from taggit.models import Tag

register = template.Library()

@register.inclusion_tag('blog/tag_cloud.html')
def tag_cloud():
    tags = Tag.objects.all()
    context = {'tags': tags}
    return context