import pytest
from django.urls import reverse
from djblogger.blog.models import Article

pytestmark = pytest.mark.django_db

class TestPostModel:
    def test_str_return(self,post_factory):
        post = post_factory(title="test-post")
        assert post.__str__()=="test-post"

    def test_save_method_generates_slug(self,post_factory):
        post = post_factory(title="test-post",slug="")
        post.save()
        assert post.slug == "test-post"

    def test_absolute_url(self,post_factory):
        post = post_factory(title="test-post")
        final_result = reverse('article-detail',args=[post.slug])
        assert post.get_absolute_url() == final_result
