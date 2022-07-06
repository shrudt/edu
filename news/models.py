from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Tags(models.Model):
    tag_name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags)
    title = models.CharField(max_length=60, null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    content = models.TextField(max_length=100, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
