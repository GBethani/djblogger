import factory
from django.contrib.auth.models import User
from . import models
from factory.faker import faker

fake = faker.Faker()

class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Article

    title = factory.Faker('sentence',nb_words=10)
    subtitle = factory.Faker('sentence',nb_words=10)
    slug = factory.Faker('slug')

    @factory.lazy_attribute
    def author(self):
        user = User.objects.get(username='goel')
        return user

    @factory.lazy_attribute
    def content(self):
        return fake.paragraphs(nb=3)

    status = 'published'