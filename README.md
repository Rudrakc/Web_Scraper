# Web Scraper

This is a simple web scraper written in Python that extracts price and review information from Flipkart and Amazon product pages.

## Requirements

- Python 3.x
- Requests library
- BeautifulSoup library
- Tabulate library

```
pip install -r requirements.txt
```


## Usage

1. Clone or download the repository.
2. Install the required libraries mentioned above using pip install -r requirements.txt.
3. Run the `web_scraper.py` script.
4. Enter the URLs of the Flipkart and Amazon product pages when prompted.
5. The script will scrape the price and review information from both websites and display it in a tabular format.

## Functionality

- The script extracts the price and review count of the product from both Flipkart and Amazon.
- It then compares the prices and informs you which platform offers the product at a cheaper rate.

## Note

- Make sure to provide valid URLs of Flipkart and Amazon product pages.
- This script uses a simple method to convert prices from USD to INR based on the current exchange rate fetched from Forbes. The conversion may not be completely accurate due to fluctuations in exchange rates.

---

