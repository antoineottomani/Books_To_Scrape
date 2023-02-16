import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime, date

static_url_product = "http://books.toscrape.com/catalogue/"

products_urls_list = []

def get_category(category_url):

    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    if response.status_code == 200:

        try: # Cas ou il y a d'autres pages
            pagination = soup.find("ul", class_="pager").select_one("li", class_="current").text.strip()
            total_pages = [int(char)for char in pagination.split() if char.isdigit()][-1] # Renvoie le chiffre du total des pages
            category_urls = []

            # constituer une liste avec les urls de chaque page
            for page in range(total_pages):
                page += 1
                next_page = category_url.replace("index.html", f"page-{page}.html")
                category_urls.append(next_page)

            for url in category_urls:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")

                category_products = soup.find_all("h3")

                for product in category_products:
                    # Clean the dynamic url : remove './'
                    dynamic_url_product = product.a["href"].strip("./")
                    full_url_product = static_url_product + dynamic_url_product
                    products_urls_list.append(full_url_product)
                

        except: # Cas ou il n'y a pas d'autres pages
            response = requests.get(category_url)
            category_products = soup.findAll("h3")

            for product in category_products:
                # Clean the dynamic url : remove './'
                dynamic_url_product = product.a["href"].strip("./")
                full_url_product = static_url_product + dynamic_url_product
                products_urls_list.append(full_url_product)

    return products_urls_list

all_urls_from_category = get_category("http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html")


book_attributes = [
    "product_page_url",
    "title",
    "category",
    "universal_product_code",
    "price_excluding_tax",
    "price_including_tax",
    "number_available",
    "description",
    "image_url",
    "review_rating",
]

def get_book(url):
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
    menu_links = soup_book.findAll("ul", class_="breadcrumb")
    for elt in menu_links:
        links = elt.findAll("a")
        category = links[-1].text
    book_data.append(category)

    # Get informations from table
    tds = soup_book.findAll("td")
    clean_data = []
    for td in tds:
        clean_data.append(td.text)

    del clean_data[1]
    del clean_data[3]
    del clean_data[-1]

    book_data.extend(clean_data)

    # Get product_description
    description = soup_book.find("article").find("p", recursive=False)
    book_data.append(description.text)

    # Get image_url
    static_url = "http://books.toscrape.com/"
    image_tag = soup_book.find("div", class_="carousel-inner").find("img")
    image_url = static_url + image_tag["src"].strip("./")
    book_data.append(image_url)

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

# Write datas into a csv file
with open(f"output-{datetime.now()}.csv", "w", newline="") as csv_file:
    # Print into csv the headers
    writer = csv.writer(csv_file)
    writer.writerow(book_attributes)

    # Print into csv data
    for url in all_urls_from_category:
        writer.writerow(get_book(url))




