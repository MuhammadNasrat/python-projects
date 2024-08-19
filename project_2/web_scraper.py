from bs4 import BeautifulSoup
import requests

response = requests.get("https://books.toscrape.com/")
soap = BeautifulSoup(response.content, "html.parser")

books = soap.find_all("article")

for book in books:
    title = book.h3.a['title']
    rating = book.p['class'][1]
    price = book.find("p", class_="price_color").text
    print(f"Book title is : {title} ,its price is {price} and its rating is : {rating} stars.")