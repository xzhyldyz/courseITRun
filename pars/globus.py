import requests
from bs4 import BeautifulSoup

link = 'https://globus-online.kg/catalog/myaso_ptitsa_ryba/govyadina_baranina_farshi/'
site = requests.get(link)
html = BeautifulSoup(site.content, 'html.parser')
main_api = 'https://globus-online.kg'

names = html.find_all('div', class_='list-showcase__name')
sales = html.find_all('span', class_='c-prices__value')
links = html.find_all('div', class_='list-showcase__name')

link_lst = [main_api + i.find('a').get('href') for i in links]
sales_lst = [i.text for i in sales]
names_lst = [i.text for i in names]
new = list(zip(names_lst, sales_lst, link_lst))

with open('meats.txt', 'a') as file:
    for i in new:
        file.write(f"{i[0]} - {i[1]} - {i[2]} \n")
        