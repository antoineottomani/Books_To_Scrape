import requests
from bs4 import BeautifulSoup


def all_categories_urls(home_url: str) -> list:
    
    """Function description

    Args:
        home_url (str): home page url

    Returns:
        list: url of each category
    """

    static_url = "http://books.toscrape.com/"

    all_categories = []

    response = requests.get(home_url)
    soup = BeautifulSoup(response.content, "html.parser")
    
 
    categories_container = soup.find("aside", class_="sidebar")
    links = categories_container.select("li > ul > li > a")
    
    global titles_categories
    titles_categories = [title.text.strip() for title in links]
    
    for i in links:
        i = static_url + i["href"]
        all_categories.append(i)      
    
    return all_categories

