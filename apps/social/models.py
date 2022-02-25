from django.db import models


class ArticleCategory(models.Model):
    """Модель для категории публикаций"""
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Категории публикаций'
        verbose_name = 'Категория публикации'


class Article(models.Model):
    """Модель для публикаций"""
    title = models.CharField(max_length=155)
    description = models.TextField()
    poster = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'
