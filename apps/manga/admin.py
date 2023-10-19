from django.contrib import admin

from .models import Chapter, Manga, Page


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    pass


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass

