import pytest

pytestmark = pytest.mark.django_db

class TestPostModel:
    def test_str_return(self,post_factory):
        post = post_factory(title="test-post")
        assert post.__str__()=="test-post"

    def test_save_method_generates_slug(self,post_factory):
        post = post_factory(title="test-post",slug="")
        post.save()
        assert post.slug == "test-post"