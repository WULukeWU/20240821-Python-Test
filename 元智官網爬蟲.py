import requests
from bs4 import BeautifulSoup
import os

YZU_CRAWLER = os.environ['YZU_CRAWLER']

url = 'https://www.yzu.edu.tw/index.php/tw'
url_page = url[:url.find('/', url.find('//') + 2)]
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

content_divs = soup.find_all('div', class_='msg-content')

for content_div in content_divs:

    title_tag = content_div.find('h3').find('a')
    title = title_tag.text.strip() if title_tag else 'N/A'

    link = url_page + title_tag['href'] if title_tag and 'href' in title_tag.attrs else 'N/A'

    date_tag = content_div.find('div', class_='date')
    date = date_tag.text.strip() if date_tag else 'N/A'

    print(f'Title: {title}')
    print(f'Link: {link}')
    print(f'Date: {date}')
    print("-" * 40)
