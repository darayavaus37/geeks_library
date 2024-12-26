import requests
from bs4 import BeautifulSoup as BS4

URL = 'https://jut.su'
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

# 1. Сделать запрос
def get_html(url, params=""):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

# 2. Получить данные
def get_data(html):
    bs = BS4(html, features="html.parser")
    items = bs.find_all('div', class_="all_anime_content anime_some_margin")
    jutsu_list = []
    for item in items:
        title = item.find("div", class_="aaname").get_text(strip=True)
        
        # Проверяем, найден ли div с изображением
        image_div = item.find("div", class_="all_anime_image")
        if image_div:
            img_tag = image_div.find("img")
            if img_tag and img_tag.get("src"):
                image = URL + img_tag.get("src")
                jutsu_list.append(
                    {
                        "title": title,
                        "image": image
                    }
                )
            else:
                jutsu_list.append(
                    {
                        "title": title,
                        "image": None  # Если изображение не найдено, добавляем None
                    }
                )
        else:
            jutsu_list.append(
                {
                    "title": title,
                    "image": None  # Если div с изображением не найден, добавляем None
                }
            )
    return jutsu_list

# 3. Функция парсинга
def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        jutsu_list2 = []
        for page in range(1, 2):
            response = get_html("https://jut.su/anime/", params={"page": page})
            jutsu_list2.extend(get_data(response.text))
        return jutsu_list2
    else:
        raise Exception('Error in parsing')

# print(parsing())


# import requests
# from bs4 import BeautifulSoup as BS4

# URL = 'https://jut.su/anime'

# HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
# }

# def get_html(url, params=""):
#     request = requests.get(url, headers=HEADERS, params=params)

# def get_data(html):
#     bs = BS4(html, features="html.parser")
#     items = bs.find_all('div', class_='all_anime_content anime_some_margin')
#     jutsu_list = []
#     for item in items:
#         title = item.find("div", class_="aaname").get_text(strip=True)
#         series = item.find("div", class_="aailines").get_text(strip=True)
#         image = URL + item.find("all_anime_image").find("img").get("src")
#         jutsu_list.append(
#             {
#                 "title": title,
#                 "image": image,
#                 "series": series
#             }
#         )
#         return jutsu_list
    

# def parsing():
#     response = get_html(URL)
#     if response.status_code == 200:
#         jutsu_list2 = []
#         for page in range(1, 2):
#             response = get_html("https://jut.su/anime/", params={"pages": page })
#             return jutsu_list2
#     else:
#         raise Exception('Error parsing')
    