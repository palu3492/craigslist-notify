from urllib.request import Request, urlopen
import urllib.request
import pprint
import bs4 as bs
from bs4 import BeautifulSoup as bs4


# source = urllib.request.urlopen("https://minneapolis.craigslist.org/search/sss?query=car&sort=rel").read()
req = Request("https://minneapolis.craigslist.org/search/sss?query=car&sort=rel", headers={'User-Agent': 'Mozilla/5.0'})
source = urlopen(req).read()
soup = bs.BeautifulSoup(source, 'html.parser')
soup.find('ul', class_='rows')
listings = soup.find_all('li', class_='result-row')
for listing in listings[:1]:
    print(listing)
    # title = listing.find('a', class_='result-title hdrlnk').getText().strip()
    # price = listing.find('span', class_='result-price').getText().strip()
    # date = listing.find('time', class_='result-date').getText().strip()
    # location = listing.find('span', class_='result-hood').getText().strip()
    # image = listing.find('img')
    # print(title)
    # print(price)
    # print(date)
    # print(location)
    # print(image)
    # print()
