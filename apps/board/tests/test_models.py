from django.test import TestCase

from apps.social.models import ArticleCategory


class TestArticleCategoryModel(TestCase):

    def test_create_article(self):
        category = ArticleCategory.objects.create(title='первая тестовая категория')
        self.assertEqual(category.title, 'первая тестовая категория')

    def test_create_article_count(self):
        ArticleCategory.objects.create(title='тестовая категория')
        article_count = ArticleCategory.objects.count()
        self.assertEqual(article_count, 1)
