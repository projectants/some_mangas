from django.db import models

from .manga import Manga


class Chapter(models.Model):
    manga = models.ForeignKey(
        Manga,
        on_delete=models.CASCADE
    )
    number = models.IntegerField()
    slug = models.SlugField(
        max_length=255,
        unique=True
    )

    def __str__(self):
        return f'{self.manga.title} - {self.number}'

    class Meta:
        verbose_name = 'Capítulo'
        verbose_name_plural = 'Capítulos'
        ordering = ['number']
