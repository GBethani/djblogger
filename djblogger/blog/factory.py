import factory, random
from django.contrib.auth.models import User
from . import models
from factory.faker import faker
from taggit.models import Tag

fake = faker.Faker()

taglist = ["Python","Django","Git","Back-end","Front-end","Deploy"] 

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

    @factory.post_generation
    def tags(self,create,extracted,**kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of tags was passed, use them.
            for tag in extracted:
                self.tags.add(tag)
        else:
            # Shuffle the taglist and take a random number of tags.
            shuffled_taglist = list(taglist)  # Create a copy to avoid modifying the original list
            random.shuffle(shuffled_taglist)
            # Specify the number of tags you want to take
            num_tags = random.randint(0,len(shuffled_taglist))
            for tag in shuffled_taglist[:num_tags]:
                self.tags.add(tag)