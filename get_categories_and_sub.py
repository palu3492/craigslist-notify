import urllib.request
import bs4 as bs
import re

source = urllib.request.urlopen("https://minneapolis.craigslist.org/").read()
soup = bs.BeautifulSoup(source, "lxml")
categories = soup.find_all("div", class_="cats")
categories_to_sub_categories = {}
for cat in categories:
    name = cat.find_previous_sibling('h4').getText()
    categories_to_sub_categories[name] = []
    uls = cat.find_all("ul")
    for ul in uls:
        lis = ul.find_all("li")
        for li in lis:
            categories_to_sub_categories[name].append(li.getText())
print(categories_to_sub_categories)



#div cats
#find all ul
#loop through ul