from pathlib import Path
import csv
from datetime import datetime
import requests
from time import time

# Imports my own modules
from scraping import all_categories_urls, book_attributes, book, all_category_urls


home_url = "http://books.toscrape.com/index.html"

response = requests.get(home_url)

if response.status_code == 200:

    list_categories = [all_category_urls(element) for element in all_categories_urls(home_url)]
    
    # Create directory for csv file output
    csv_directory = Path.cwd() / "Data/Csv"
    csv_directory.mkdir(parents=True, exist_ok=True)

    for category_item in list_categories:
        
            with open(csv_directory / f"output_{datetime.now()}.csv", "w", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(book_attributes)

                for i in category_item:
                    writer.writerow(book(i))




    


    


  

  

                


                
        
        