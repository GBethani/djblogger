import pytest
from django.contrib.admin.sites import AdminSite
from djblogger.blog.admin import ArticleAdmin
from djblogger.blog.models import Article

pytestmark = pytest.mark.django_db

class TestArticleAdmin:
    def setup_method(self):
        self.admin_site = AdminSite()
        self.article_admin = ArticleAdmin(Article,self.admin_site)

    def test_short_title(self,post_factory):
        post = post_factory(title="This is a very long title that exceeds 30 characters")
        result = self.article_admin.short_title(post)
        final_result = "This is a very long title that......"
        assert result == final_result

    def test_tag_list(self,post_factory):
        post = post_factory()
        result = self.article_admin.tag_list(post)
        final_result = ", ".join(post.tags.values_list("name", flat=True))
        assert result == final_result
