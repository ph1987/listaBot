import requests
from bs4 import BeautifulSoup as bs

url = 'https://m.facebook.com/pg/casadamatriz/events'

page = requests.get(url)
soup = bs(page.text, 'html.parser')
bvs = soup.findAll("span", {"class": "bv"})

#brs = soup.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['br'])
#bus = soup.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['bu'])

eventList = []

for bv in bvs:
	for a in bv.find_all('a', href=True):
		x = a['href'].split('?')
		eventList.append(x[0])  #/events/9999999999

url2 = 'https://m.facebook.com/' + eventList[0]
page2 = requests.get(url2)
soup2 = bs(page2.text, 'html.parser')
xx = soup2.findAll("div", {"class": "ct cu cg"})
yy = soup2.findAll("div", {"class": "cv cw cg"})
title = soup2.find('title').text

for x in xx:
	print(x.text)

for y in yy:
	print(y.text)

print(title)
print(url2)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

'''
for br in brs:
	print(br.get_text())

print(soup)

zz = soup2.findAll("header", {"class": "_5ro_"})

url3 = 'https://www.facebook.com/events/2405532806178437'
page3 = requests.get(url3)
soup3 = bs(page3.text, 'html.parser')
zz = soup3.findAll("span", {"class": "_5z74"})

print(soup3)

'''



''' solução com selenium

from bs4 import BeautifulSoup
from selenium import webdriver

url = "http://legendas.tv/busca/walking%20dead%20s03e02"
browser = webdriver.PhantomJS()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
a = soup.find('section', 'wrapper')

'''


'''

<a class="bi bj bk" href="/casadamatr
iz/photos/gm.2410098562560588/2734999826515221/?type=3&amp;source=44"><img class
="bl bm k" src="https://scontent-gru2-2.xx.fbcdn.net/v/t1.0-0/cp0/e15/q65/c0.2.9
60.537a/s320x320/65109378_2734999833181887_7352555321476251648_n.jpg?_nc_cat=100
&amp;_nc_oc=AQnZRiWd4lXPDpd90bEzvloAa_BRH--y6DtTw1oVUcZHX7mOOsHB0ZmYnEjyDsAgJNs&
amp;_nc_ht=scontent-gru2-2.xx&amp;oh=ac31db73b84b20d05bf8d3c0903ec3a9&amp;oe=5DB
6B411"/>

'''