from django.db import models


def upload_to(instance, filename):
    return f'covers/{instance.title}/{filename}'


class Manga(models.Model):
    cover = models.ImageField(
        upload_to=upload_to,
    )
    title = models.CharField(
        max_length=255
    )
    synopsis = models.TextField()
    author = models.CharField(
        max_length=255
    )
    slug = models.SlugField(
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Mangá'
        verbose_name_plural = 'Mangás'
        ordering = ['title']
