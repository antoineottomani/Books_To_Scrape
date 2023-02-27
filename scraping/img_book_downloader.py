import requests
import shutil
from bs4 import BeautifulSoup
from datetime import datetime

def download_img(product_url):
    response = requests.get(product_url)
    soup = BeautifulSoup(response.content, "html.parser")

    static_url = "http://books.toscrape.com/"
    image_tag = soup.find("div", class_="carousel-inner").find("img")
    image_url = static_url + image_tag["src"].strip("./")
    
    image_result = requests.get(image_url, stream = True)
    image_result.raw.decode_content = True

    with open(f"Image-{datetime.now()}.jpg", 'wb') as f:
        shutil.copyfileobj(image_result.raw, f)