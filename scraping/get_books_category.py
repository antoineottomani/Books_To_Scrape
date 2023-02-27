import requests
from bs4 import BeautifulSoup

def get_one_page_book_url(category_url):
    static_url_product = "http://books.toscrape.com/catalogue/"
    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, "html.parser")

    category_products = soup.findAll("h3")

    products_urls_list = []

    for product in category_products:
        # Clean the dynamic url : remove './'
        dynamic_url_product = product.a["href"].strip("./")
        full_url_product = static_url_product + dynamic_url_product
        products_urls_list.append(full_url_product)
    
    return products_urls_list



def all_category_urls(category_url: str) -> list:

    """Function description
     Args:
        category_url (str): url of a category

    Returns:
        list: all books's urls from a specific category
    """
    
    static_url_product = "http://books.toscrape.com/catalogue/"
    products_urls_list = []
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
                products_urls_list.extend(get_one_page_book_url(url))
                

        except: # Cas ou il n'y a pas d'autres pages
            products_urls_list = get_one_page_book_url(category_url)

    return products_urls_list