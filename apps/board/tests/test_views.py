import io

from django.core.files.images import ImageFile
from django.test import TestCase
from django.urls import reverse

from apps.social.models import Article, ArticleCategory


class TestArticleView(TestCase):

    def test_get_article_list(self):
        url = reverse('articles-url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_article_single(self):
        cat1 = ArticleCategory.objects.create(title='тестовая категория')

        image = ImageFile(io.BytesIO(b'some-file'), name='test-image.jpg')
        article = Article.objects.create(category=cat1, title='тестовый заголвоко', description='qwerty',
                                         poster=image)
        url = reverse('articles-single-url', kwargs={'pk': article.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
