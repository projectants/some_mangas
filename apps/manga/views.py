from django.shortcuts import render

from .models import Manga


def home(request):
    return render(request, 'manga/pages/home.html',
                  context={
                      "mangas": Manga.objects.all(),
                      "name": "Some-Mangás"
                  }
                  )
