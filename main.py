import requests
from bs4 import BeautifulSoup
import csv

data_book = {}

# STEP 2
def get_book(url):
    r = requests.get(url)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')

        # Get product_page_url 
        product_page_url = r.url
        data_book["product_page_url"] = product_page_url
        
        # Get title
        title = soup.find("h1")
        data_book["title"] = title.text

        # Get category
        menu_links = soup.findAll("ul", class_="breadcrumb")
        for elt in menu_links:
            links = elt.findAll("a")
            category = links[-1].text
        # Add category to data_book
        data_book["category"] = category

        # Get informations from table
        tds = soup.findAll("td")
        clean_data = []
        for td in tds:
            clean_data.append(td.text)

        data_book["universal_product_code"] = clean_data[0]
        data_book["price_excluding_tax"] = clean_data[2]
        data_book["price_including_tax"] = clean_data[3]
        data_book["number_available"] = clean_data[-2]

        # Get product_description
        description = soup.find("article").find("p", recursive=False).text
        data_book["product_description"] = description

        # Get image_url
        static_url = "http://books.toscrape.com/"
        image_tag = soup.find("div", class_="carousel-inner").find("img")
        image_url = static_url + image_tag["src"].strip("./")
        data_book["image_url"] = image_url
    
    
# Getting data from one book
get_book("http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html")

# Write datas into a csv file
with open('output.csv', "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=data_book.keys())
    writer.writeheader()
    writer.writerow(data_book)


