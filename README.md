# Web Scraper

This project contains a Python script for web scraping. The `scraper.py` file exports a function `scrape_data` which takes a URL as input and returns a list of dictionaries containing the scraped data. The function uses the `requests` library to make HTTP requests and the `BeautifulSoup` library to parse the HTML response.

## Dependencies

The project requires the following dependencies, which can be installed using `pip`:

- requests
- beautifulsoup4

To install the dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

To use the web scraper, import the `scrape_data` function from `scraper.py` and call it with a URL as input. For example:

```python
from scraper import scrape_data

url = 'https://example.com'
data = scrape_data(url)
print(data)
```

The `scrape_data` function returns a list of dictionaries, where each dictionary represents a piece of scraped data. The keys of the dictionary correspond to the fields of the data, and the values correspond to the values of the data.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.