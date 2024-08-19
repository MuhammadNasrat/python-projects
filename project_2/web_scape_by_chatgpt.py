from bs4 import BeautifulSoup
import requests

# Send a GET request to the website
url = 'https://books.toscrape.com/'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all articles containing book information
    books = soup.find_all('article')
    
    # Loop through each book and extract title, rating, and price
    for book in books:
        title = book.h3.a['title']
        rating = book.p['class'][1]
        price = book.find('p', class_='price_color').text
        
        # Print the extracted information
        print(f"Title: {title}, Rating: {rating}, Price: {price}")
else:
    print('Failed to retrieve the webpage')
