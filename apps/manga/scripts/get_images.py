from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def list_images(link):
    images = []
    options = Options()
    options.headless = True
    options.page_load_strategy = 'normal'
    driver = webdriver.Firefox(options=options)

    driver.get(link)
    elements = driver.find_elements(By.TAG_NAME, 'img')

    for elem in elements:
        href = elem.get_attribute('src')
        if href is not None and 'https://mangaonline.biz/wp-content/uploads/' in href:
            images.append(href)
    driver.quit()
    return images


# imgs = list_images(
#     'https://mangaonline.biz/capitulo/blue-lock-capitulo-1/')

# for x in imgs[0:len(imgs)-6]:
#     print(x)
