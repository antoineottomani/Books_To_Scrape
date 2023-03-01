import requests
import shutil
from bs4 import BeautifulSoup
from pathlib import Path


book_attributes = [
    "product_page_url",
    "title",
    "category",
    "universal_product_code",
    "price_excluding_tax",
    "price_including_tax",
    "number_available",
    "description",
    "review_rating",
    "review_rating",
    "image_url",
]


def book(url: str) -> list:
    
    """Function description
    Args:
        url (str): url of a book

    Returns:
        list: book's data declared in 'book_attributes'
    """
    
    book_data = []

    response_book = requests.get(url)
    soup_book = BeautifulSoup(response_book.content, "html.parser")

    # Get product_page_url
    product_page_url = response_book.url
    book_data.append(product_page_url)

    # Get title
    title = soup_book.find("h1")
    book_data.append(title.text)

    # Get category
    menu_links = soup_book.find_all("ul", class_="breadcrumb")
    for elt in menu_links:
        links = elt.find_all("a")
        category = links[-1].text
    book_data.append(category)

    # Get informations from table
    tds = soup_book.findAll("td")
    clean_data = []
    for td in tds:
        clean_data.append(td.text)

    # Delete not necessary data
    del clean_data[1]
    del clean_data[3]
    del clean_data[-1]

    book_data.extend(clean_data)

    # Get product_description
    description = soup_book.find("article").find("p", recursive=False)
    if description:
        book_data.append(description.text)
    else:
        book_data.append("")

    # Get image_url
    static_url = "http://books.toscrape.com/"
    image_tag = soup_book.find("div", class_="carousel-inner").find("img")
    image_url = static_url + image_tag["src"].strip("./")
    book_data.append(image_url)

    # Download image
    img_directory = Path.cwd() / "Data/Img"
    img_directory.mkdir(parents=True, exist_ok=True)

    image_result = requests.get(image_url, stream = True)
    image_result.raw.decode_content = True

    with open(img_directory / f"{category}_{title.text.replace('/', '_')}.jpg", 'wb') as f:
            shutil.copyfileobj(image_result.raw, f)
        
    # Get review_rating
    notation_container = soup_book.find("div", class_="product_main").find("p", class_="star-rating")
    nb_stars = notation_container["class"][-1]
    
    match nb_stars:
        case "One":
            nb_stars = 1
        case "Two":
            nb_stars = 2
        case "Three":
            nb_stars = 3
        case "Four":
            nb_stars = 4
        case "Five":
            nb_stars = 5

    book_data.append(nb_stars)

    return book_data

