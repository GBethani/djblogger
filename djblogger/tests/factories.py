import factory
from django.contrib.auth.models import User
from djblogger.blog import models

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "test"
    password = "test"
    is_superuser = True
    is_staff = True

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Article

    title =    "x"
    subtitle = "x"
    slug =     "x"
    content =  "x"
    author =   factory.SubFactory(UserFactory)
    status =   "x"