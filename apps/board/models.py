from django.db import models


class PublicationAd(models.Model):
    """Модель для Объявлений"""

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')  # на практике используется DecimalField
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан в')  # записывается текущее время при создании записи

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'

    def __str__(self):
        return self.title
