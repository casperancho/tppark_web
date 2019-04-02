from django.db import models

class Article(models.Model):
    title: models.CharField(
        max_length=255, verbose_name="Название")
    text: models.TextField(verbose_name="Текст")
    is_published: models.BooleanField(verbose_name="Опубликована")

