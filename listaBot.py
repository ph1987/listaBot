import requests
from bs4 import BeautifulSoup as bs

urList = []
urList.append('https://m.facebook.com/pg/casadamatriz/events')

for url in urList:
	eventsList = requests.get(url)
	eventsListSourceCode = bs(eventsList.text, 'html.parser')
	bvClassInEventsListSourceCode = eventsListSourceCode.findAll("span", {"class": "bv"})

	eventList = []

	for bvClass in bvClassInEventsListSourceCode:
		for a in bvClass.find_all('a', href=True):
			x = a['href'].split('?')
			eventList.append(x[0])  							    #/events/9999999999

	eventUrl = 'https://m.facebook.com/' + eventList[0]
	eventPage = requests.get(eventUrl)
	eventPageSourceCode = bs(eventPage.text, 'html.parser')
	
	eventDateFullAndLocationName = eventPageSourceCode.findAll("div", {"class": "ct cu cg"})
	eventTimeUntilAndStreetAddress = eventPageSourceCode.findAll("div", {"class": "cv cw cg"})
	eventTitle = eventPageSourceCode.find('title').text

	eventDateFull = eventDateFullAndLocationName[0].text
	eventLocationName = eventDateFullAndLocationName[1].text
	eventTimeUntil = eventTimeUntilAndStreetAddress[0].text
	eventStreetAddress = eventTimeUntilAndStreetAddress[1].text
		
	print(eventDateFull)
	print(eventLocationName)
	print(eventTimeUntil)
	print(eventStreetAddress)
	print(eventTitle)
	print(eventUrl)

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