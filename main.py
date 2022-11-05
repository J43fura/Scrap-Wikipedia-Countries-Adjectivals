from bs4 import BeautifulSoup
import json
import requests

#Wikipedia countries and their respective Adjectivals

#URL = "https://en.wikipedia.org/wiki/List_of_adjectival_and_demonymic_forms_for_countries_and_nations"
#page = requests.get(URL)
#soup = BeautifulSoup(page.content, "html.parser")
#soup=BeautifulSoup(page.content, "html.parser")

file = open("countries.html", "r")
soup=BeautifulSoup(file.read(), "html.parser")
results = soup.find("tbody")


i=0
dict = {}

trs = results.find_all("tr")

for tr in trs:
    tds = tr.find_all("td")
    D = []
    C = tds[0].text
    if C.find('[') != -1:
        C = C[:C.find('[')]


    if (tds[1].find_all("li")):
        lis=tds[1].find_all("li")
        for li in lis:
            ass = li.find_all("a")
            for a in ass:
                D.append(a.text)
                break
    else:
        D = tds[1].text
    dict[C] = D

print(dict)

with open("Countries And Adjectivals.json", "w") as outfile:
    json.dump(dict, outfile)

