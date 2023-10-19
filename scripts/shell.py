import concurrent.futures
from io import BytesIO

import requests

from apps.manga.models import Chapter, Manga, Page
from apps.manga.scripts.get_chapters import list_chapters
from apps.manga.scripts.get_images import list_images


def download_image(url):
    response = requests.get(url)
    return response.content


def run():
    manga = Manga.objects.create(title="Hunter x Hunter",
                                 synopsis="Os caçadores são uma raça especial, dedicada a rastrear tesouros, feras mágicas e até outros homens. Mas essas atividades exigem uma licença, e menos de uma em cem mil pode passar no exaustivo exame de qualificação. Aqueles que passam ganham acesso a áreas restritas, armazenamentos incríveis de informações e o direito de se chamarem Caçadores.",
                                 author="Yoshihiro Togashi",
                                 slug="hunter-x-hunter")

    cover = requests.get(
        'https://d1b14unh5d6w7g.cloudfront.net/B07TZNQB5S.01.S001.JUMBOXXX.jpg?Expires=1694370636&Signature=dHWRCnQyd5ECgVCYRGJYz7jLuHI1~~HLalMf60jtVQn4-KpAV0TbdDJUd1TWAv7OJEnUD1Wn-K3IEYnyQ0TCRKDRqO3q3Iu73Q-VdX9-5a-6T3PIPN7jeYkeznHZbJnFDJ37K2MLART5XLc1~uYB0RRwc7H47vm143aUQTngc18_&Key-Pair-Id=APKAIUO27P366FGALUMQ')

    with BytesIO(cover.content) as cover:
        manga.cover.save("01.jpg", cover)
    manga.save()

    chapters = list_chapters(
        "https://mangaonline.biz/manga/hunter-x-hunter/")

    i = 1
    j = 1

    for x in chapters[0:len(chapters)-1]:
        chapter = Chapter.objects.create(
            manga=manga, number=i, slug=f"hunter-x-hunter-{i}")
        chapter.save()

        print(f'Chapter {i} Cadastred')
        i += 1

        images = list_images(x)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(download_image, img_url)
                       for img_url in images[:len(images) - 6]]

            for future in concurrent.futures.as_completed(futures):
                img_content = future.result()
                page = Page.objects.create(chapter=chapter, number=j)

                with BytesIO(img_content) as img:
                    page.image.save(f"{j}.jpg", img, save=False)

                page.save()
                print(f'Page {j} Cadastred')
                j += 1
            j = 1
