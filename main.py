import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.100bestbooks.ru"

page = requests.get(url)

text = page.text
soup = BeautifulSoup(text, "lxml")

print(soup)

print(soup.prettify())

soup.find_all("table")

print(len(soup.find_all("table"))) # всего table

print(len(soup.find_all("table", {"class": "table-rating"}))) # всего table class": "table-rating

table = soup.find_all("table", {"class": "table-rating"})[0]

names = []
years = []
for t in table.find_all("td", {"class":"vline"}, style="text-align: left"):
    names.append(t.text)
    print(t.text)

print(names)

for t in table.find_all("td", {"class":"vline-year"}):
    years.append(t.text)
    print(t.text)

print(years)

print(len(names))
print(len(years))

df = pd.DataFrame({'Произведение': names, 'Год': years})

print(df.head())

df.to_csv("Top_100_books.csv")



