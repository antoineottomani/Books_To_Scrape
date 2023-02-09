import requests
from bs4 import BeautifulSoup
import csv

static_url_product = "http://books.toscrape.com/catalogue/"

# Gets one category by url & returns all urls books of this category
def get_category(category_url):

    products_urls_list = []

    response = requests.get(category_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Get all h3
        category_products = soup.findAll("h3")
        for product in category_products:
            # Clean the dynamic url : remove './'
            dynamic_url_product = product.a["href"].strip("./")
            full_url_product = static_url_product + dynamic_url_product
            products_urls_list.append(full_url_product)
        
    return products_urls_list


urls_from_category = get_category("http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html")


book_attributes = ["product_page_url", 
                    "title", 
                    "category", 
                    "universal_product_code", 
                    "price_excluding_tax",
                    "price_including_tax", 
                    "number_available", 
                    "description",
                    "image_url",
                    "review_rating"
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
    description = soup_book.find("article").find("p", recursive=False).text
    book_data.append(description)

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
with open('output.csv', "w", newline="") as csv_file:

    # Print into csv the headers
    writer = csv.writer(csv_file)
    writer.writerow(book_attributes)

    # Print into csv data
    for url in urls_from_category:
        writer.writerow(get_book(url))

