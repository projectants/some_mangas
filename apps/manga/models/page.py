from django.db import models

from .chapter import Chapter


def upload_to(instance, filename):
    return f'pages/{instance.chapter.manga.title}/{instance.chapter.slug}/{filename}'


class Page(models.Model):
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to=upload_to,
    )
    number = models.IntegerField()

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['number']
