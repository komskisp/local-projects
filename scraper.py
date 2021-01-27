from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.com/s?k=coffee+grinder&ref=nb_sb_noss_2'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(class_='a-link-normal a-text-normal')
print(title)
