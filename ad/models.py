from django.conf import settings
from django.db import models


class Ad(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name='Название товара'
    )

    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )

    description = models.CharField(
        max_length=1500,
        blank=True,
        null=True,
        verbose_name='Описание товара'
    )

    author = models.ForeignKey(
        settings.AUTH_USER.MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    created_at


class Comment(models.Model):
    text
    author
    ad
    created_at
