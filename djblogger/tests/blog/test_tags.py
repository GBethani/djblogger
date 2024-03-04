import pytest
from django.urls import reverse
from django.test import Client
from djblogger.blog.models import Article

pytestmark = pytest.mark.django_db

class TestTaggedPosts:
    def test_url(self,post_factory):
        post = post_factory(title="test-post",tags=['test-tag'])
        url = reverse('tagged-posts',kwargs={'tag':'test-tag'})
        response = Client().get(url)
        assert response.status_code == 200
        