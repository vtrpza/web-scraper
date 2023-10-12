import requests
from bs4 import BeautifulSoup


def scrape_data(url):
    """
    Scrapes data from a given URL and returns a list of dictionaries containing the scraped data.
    """
    # Make HTTP request
    response = requests.get(url)

    # Parse HTML response
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find relevant data
    data = []
    for item in soup.find_all('div', class_='item'):
        title = item.find('h2').text.strip()
        price = item.find('span', class_='price').text.strip()
        description = item.find('p', class_='description').text.strip()
        data.append({'title': title, 'price': price,
                    'description': description})

    return data
