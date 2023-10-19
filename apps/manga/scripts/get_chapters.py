from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def list_chapters(link):
    lista_capitulos = []
    capitulos = []

    options = Options()
    options.headless = True
    options.page_load_strategy = 'normal'
    driver = webdriver.Firefox(options=options)

    site = link
    driver.get(site)

    elements = driver.find_elements(By.TAG_NAME, 'a')

    for elem in elements:
        href = elem.get_attribute('href')
        if href is not None and 'capitulo' in href:
            lista_capitulos.append(href)

    driver.quit()

    for link in lista_capitulos:
        capitulos.append(link)

    capitulos = capitulos[len(capitulos):0:-1]

    return capitulos


# lista = list_chapters('https://mangaonline.biz/manga/blue-lock/')
# for x in lista[0:len(lista)-1]:
#     print(x)
