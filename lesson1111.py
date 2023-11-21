import requests
from bs4 import BeautifulSoup as bs

re1 = requests.get("https://sinoptik.ua/")
html = bs(re1.text, "html.parser")
data = html.find_all('div', class_='max')
data1 = html.find_all('p', class_='day-link')
data2 = html.find_all('a', class_='day-link')
temps = []
days = []
for i in data:
  temps.append(i.span.text)
for i in data1:
  days.append(i.text)
for i in data2:
  days.append(i.text)
for i in range(len(temps) - 1):
  print(days[i], temps[i])
