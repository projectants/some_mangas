import requests


def download_image(titulo: str, link: str):
    with open(f'{titulo}.jpg', 'wb') as imagem:
        resposta = requests.get(f"{link}", stream=True)

        if not resposta.ok:
            print("Ocorreu um erro, status:", resposta.status_code)
        else:
            for dado in resposta.iter_content(1024):
                if not dado:
                    break

                imagem.write(dado)

            print("Imagem salva! =)")


download_image(
    '01', 'https://static.wikia.nocookie.net/bluelock/images/7/77/JP_Volume_1.png/revision/latest?cb=20191026192410')
