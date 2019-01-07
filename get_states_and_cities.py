import urllib.request
import bs4 as bs
import re

search_term = "cars"
source = urllib.request.urlopen("https://www.craigslist.org/about/sites").read()
soup = bs.BeautifulSoup(source, "lxml")
boxes = soup.find("div", class_="colmask").find_all("div", class_=re.compile("box box_.*"))
all = {}
for box in boxes:
    names = soup.find_all("h4")
    regions_cons = soup.find_all("ul")
    for i in range(len(names)):
        name = names[i].getText()
        all[name] = []
        region_con = regions_cons[i]
        for w in region_con.find_all("li"):
            all[name].append(w.getText())
print(all)
