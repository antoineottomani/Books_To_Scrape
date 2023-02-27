from datetime import datetime
from pathlib import Path
#from bs4 import BeautifulSoup
import csv
#import requests

# Imports my own modules
from scraping import all_categories_urls, book_attributes, book, all_category_urls

home_url = "http://books.toscrape.com/index.html"
list_categories = [all_category_urls(element) for element in all_categories_urls(home_url)]

for category in list_categories:
      with open(f"output-{datetime.now()}.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(book_attributes)
            
            # Write each book's data of a category into a csv file
            for line in category:
                writer.writerow(book(line))
            