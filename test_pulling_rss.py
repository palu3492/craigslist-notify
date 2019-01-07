from urllib.request import Request, urlopen
import urllib.request
import pprint
import bs4 as bs
from bs4 import BeautifulSoup as bs4


for i in range(10000):
    source = urllib.request.urlopen("https://minneapolis.craigslist.org/search/sss?format=rss&query=lexus&sort=rel").read()
    print(i)
    # source=str(source)
    # soup = bs.BeautifulSoup(str(source), 'xml')
    # html = bs4(source, 'html.parser')
    # print(html.prettify())