import requests
from bs4 import BeautifulSoup as BS

#мы скачиваем страницу как html
url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
req =  requests.get(url)
src = req.text
# with open('index.html', 'w') as file:
#     file.write(src)

# мы будем работать со скаченным html
with open('index.html') as file:
     src = file.read()

soup = BS(src, 'lxml')
all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
all_categories_dict = {}
for item in all_products_hrefs:
     item_text = item.text
     item_href = 'https://health-diet.ru'+item.get('href')
     all_categories_dict[item_text]=item_href    

