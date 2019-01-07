import urllib.request
import bs4 as bs
import re

search_term = "cars"
source = urllib.request.urlopen("https://www.craigslist.org/about/sites").read()
soup = bs.BeautifulSoup(source, "lxml")
usa = soup.find("div", class_="colmask")
uls = usa.find_all("ul")
city_codes = {}
for ul in uls:
    lis = ul.find_all("li")
    for li in lis:
        city_codes[li.getText()] = li.find("a")["href"].split("/")[2].split(".")[0]
print(city_codes)
