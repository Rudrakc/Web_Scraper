import math
import requests
from tabulate import tabulate
from bs4 import BeautifulSoup


def strToInt(num):
    extracted_number = ""
    for char in num:
        if char.isdigit():
            extracted_number += char
        if char == ".":
            break
    return extracted_number


# Conerting $ to inr
def convert(dollar, headers):
    url = "https://www.forbes.com/advisor/money-transfer/currency-converter/usd-inr/"
    response = requests.get(url, headers=headers)
    with open("data/dollarToInr.html", "w") as f:
        f.write(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    inr = soup.select("span.amount")[0].get_text()
    return math.floor(float(strToInt(dollar)) * float(inr))


flipkart_url = input("Enter the Flipkart URL: ")
amazon_url = input("Enter the amazon.com URL: ")
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}
print("\t\t--------Price Scrapper--------")
data = []

# Flipkart scrapping
try:
    response = requests.get(flipkart_url, headers=headers)
    with open("data/flipkart.html", "w") as f:
        f.write(response.text)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        price_flipkart = soup.select("div._30jeq3._16Jk6d")[0].get_text()
        new_data = [
            "Flipkart",
            f"₹{strToInt(price_flipkart)}",
            f"{strToInt(soup.select('span._2_R_DZ')[0].select('span')[1].get_text())} ratings",
        ]
        data.append(new_data)
except Exception as e:
    print(f"Failed to retrieve the Flipkart page.")

# Amazon scrapping
try:
    response2 = requests.get(amazon_url, headers=headers)
    with open("data/amazon.html", "w") as f:
        f.write(response2.text)
    if response2.status_code == 200:
        soup2 = BeautifulSoup(response2.text, "html.parser")
        price_amazon = soup2.select("span.a-price-whole")[0].get_text()
        new_data = [
            "Amazon",
            f"₹{convert(price_amazon,headers)}",
            f"{soup2.find(id='acrCustomerReviewText').get_text()}",
        ]
        data.append(new_data)
except Exception as e:
    print(f"Failed to retrieve the Flipkart page.")

topRow = ["Website", "Price", "Reviews"]
table = tabulate(data, topRow, tablefmt="fancy_grid")
print(table)
if int(convert(price_amazon, headers)) > int(strToInt(price_flipkart)):
    print(
        "The product is cheaper Flipkart with price: " + f"₹{strToInt(price_flipkart)}"
    )
else:
    print(
        "The product is cheaper Amazon with price: "
        + f"₹{convert(price_amazon,headers)}"
    )
