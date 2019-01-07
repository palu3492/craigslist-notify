import urllib.request
import bs4 as bs
import re

search_term = "cars"
source = urllib.request.urlopen("https://minneapolis.craigslist.org/search/sss?query=" + search_term + "&sort=rel").read()
soup = bs.BeautifulSoup(source, "lxml")

# categories = soup.find_all("div", class_=re.compile("searchgroup.*"))
searchgroup_categories = soup.find("div", class_="searchgroup categories")
main_categories = [i.getText().strip() for i in searchgroup_categories.find("ul", class_="maincats").find_all("li")]
other_categories = [i.getText().strip() for i in searchgroup_categories.find("ul", class_="othercats closed").find_all("li")]
for cat in main_categories + other_categories:
    print(cat.split(""))