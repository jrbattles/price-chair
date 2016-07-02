__author__ = "jrbattles"

import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.staples.com/OFM-Avenger-Big-and-Tall-High-Back-Leather-Office-Chair-Black/product_200226")
content = request.content
soup = BeautifulSoup(content, "html.parser")
## print(soup)
element = soup.find("span", {"class": "SEOFinalPrice", "itemprop": "price"})
string_price = element.text.strip()  ## $494.59

price_without_symbol = string_price[1:]
price = float(price_without_symbol)

if price < 400:
    print("You should buy the chair!")
    print("The current price is {}.".format(string_price))
else:
    print("Do not buy!! the chair is too expensive!")
    print("The current price is {}.".format(string_price))



## http://www.staples.com/OFM-Avenger-Big-and-Tall-High-Back-Leather-Office-Chair-Black/product_200226
