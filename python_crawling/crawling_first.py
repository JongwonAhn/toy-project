import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0199&date=20220504'
html = requests.get(url)
#print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
#print(soup.select_one('body > div > div.sect-showtimes > ul > li > div > div.info-movie > a > strong'))
title_list = soup.select('div.info-movie')
for i in title_list:
    print(i.select_one('a > strong').text.strip())
