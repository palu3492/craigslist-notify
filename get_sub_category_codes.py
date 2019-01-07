import urllib.request
import bs4 as bs
import re

source = urllib.request.urlopen("https://minneapolis.craigslist.org/").read()
soup = bs.BeautifulSoup(source, "lxml")
categories = soup.find_all("div", class_="cats")
sub_categories_to_codes = {}
for cat in categories:
    cat_name = cat.find_previous_sibling('h4').getText()
    if cat_name != "discussion forums":
        uls = cat.find_all("ul")
        for ul in uls:
            lis = ul.find_all("li")
            for li in lis:
                name = li.getText()
                url = li.find("a")["href"].split("/")
                sub_categories_to_codes[name] = url[len(url)-1]
print(sub_categories_to_codes)



#div cats
#find all ul
#loop through ul