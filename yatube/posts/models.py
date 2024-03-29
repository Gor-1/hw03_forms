from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    # Модель Group для сообществ

    title = models.CharField(
        max_length=200,
        verbose_name='Название группы'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='Ссылка'
    )
    description = models.TextField(
        verbose_name='Описание группы'
    )

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )

    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        related_name='group_list',
        on_delete=models.SET_NULL,
        verbose_name='Группа'
    )

    class Meta:
        ordering = ['-pub_date']
