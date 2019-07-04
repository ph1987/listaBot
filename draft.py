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

	#eventUrl = 'https://m.facebook.com/' + eventList[0]
	eventUrl = 'https://m.facebook.com/events/345097086162413'
	eventPage = requests.get(eventUrl)
	eventPageSourceCode = bs(eventPage.text, 'html.parser')
	
	eventDateFullAndLocationName = eventPageSourceCode.findAll("div", {"class": "ct cu cg"})
	eventTimeUntilAndStreetAddress = eventPageSourceCode.findAll("div", {"class": "cv cw cg"})
	eventTitle = eventPageSourceCode.find('title').text

	eventDateFull = eventDateFullAndLocationName[0].text
	eventLocationName = eventDateFullAndLocationName[1].text
	eventTimeUntilAndWeather = eventTimeUntilAndStreetAddress[0].text
	eventStreetAddress = eventTimeUntilAndStreetAddress[1].text
	
	print(eventPageSourceCode)
	#print(eventDateFull)
	#print(eventLocationName)
	#print(eventTimeUntilAndWeather)
	#print(eventStreetAddress)
	#print(eventTitle)
	#print(eventUrl)

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


'''
https://scontent-gig2-1.xx.fbcdn.net/v/t1.0-0/c78.0.200.200a/p200x200/65560614_2744658635549340_7359127836914876416_n.jpg?_nc_cat=105&amp;_nc_oc=AQloSPiV91iYytfUS3Y1BWEfGMfEXhrOerY1AfZRvJlVQdxGpR77M17w45yAM5qle_M&amp;_nc_ht=scontent-gig2-1.xx&amp;oh=c77a1c4aba01c3793fd7b1a72ce60fcc&amp;oe=5DB2143A

https:\/\/scontent-gig2-1.xx.fbcdn.net\/v\/t1.0-0\/cp0\/e15\/q65\/c78.0.200.200a\/p200x200\/65560614_2744658635549340_7359127836914876416_n.jpg?_nc_cat=105&_nc_oc=AQloSPiV91iYytfUS3Y1BWEfGMfEXhrOerY1AfZRvJlVQdxGpR77M17w45yAM5qle_M&_nc_ht=scontent-gig2-1.xx&oh=fc6dd671d21b18e17111fabbefe996a6&oe=5DAD49F6

(remover as "\")



https://scontent-gig2-1.xx.fbcdn.net/v/t1.0-0/cp0/e15/q65/c78.0.200.200a/p200x200/65560614_2744658635549340_7359127836914876416_n.jpg?_nc_cat=105&_nc_oc=AQloSPiV91iYytfUS3Y1BWEfGMfEXhrOerY1AfZRvJlVQdxGpR77M17w45yAM5qle_M&_nc_ht=scontent-gig2-1.xx&oh=fc6dd671d21b18e17111fabbefe996a6&oe=5DAD49F6

https://scontent-gig2-1.xx.fbcdn.net/v/t1.0-0/cp0/e15/q65/c78.0.200.200a/p200x200/65560614_2744658635549340_7359127836914876416_n.jpg?_nc_cat=105&_nc_oc=AQloSPiV91iYytfUS3Y1BWEfGMfEXhrOerY1AfZRvJlVQdxGpR77M17w45yAM5qle_M&_nc_ht=scontent-gig2-1.xx&oh=fc6dd671d21b18e17111fabbefe996a6&oe=5DAD49F6

https://scontent-gig2-1.xx.fbcdn.net/v/t1.0-0/cp0/e15/q65/c0.2.960.537a/s320x320/65560614_2744658635549340_7359127836914876416_n.jpg?_nc_cat=105&_nc_oc=AQloSPiV91iYytfUS3Y1BWEfGMfEXhrOerY1AfZRvJlVQdxGpR77M17w45yAM5qle_M&_nc_ht=scontent-gig2-1.xx&oh=a4b0833d9be5bb5c5c3a7620bc762741&oe=5DBD5B74&#039

https\3a //scontent-gig2-1.xx.fbcdn.net/v/t1.0-0/cp0/e15/q65/c0.2.960.537a/s320x320/65560614_2744658635549340_7359127836914876416_n.jpg?_nc_cat\3d 105\26 _nc_oc\3d AQloSPiV91iYytfUS3Y1BWEfGMfEXhrOerY1AfZRvJlVQdxGpR77M17w45yAM5qle_M\26 _nc_ht\3d scontent-gig2-1.xx\26 oh\3d a4b0833d9be5bb5c5c3a7620bc762741\26 oe\3d 5DBD5B74&#039

<img class="bl bm k" src="https://scontent-gig2-1.
xx.fbcdn.net/v/t1.0-0/cp0/e15/q65/c0.2.960.537a/s320x320/65560614_27446586355493
40_7359127836914876416_n.jpg?_nc_cat=105&amp;_nc_oc=AQloSPiV91iYytfUS3Y1BWEfGMfE
XhrOerY1AfZRvJlVQdxGpR77M17w45yAM5qle_M&amp;_nc_ht=scontent-gig2-1.xx&amp;oh=a4b
0833d9be5bb5c5c3a7620bc762741&amp;oe=5DBD5B74"/>

https://scontent-gig2-1.xx.fbcdn.net/v/t1.0-0/cp0/e15/q65/c0.2.960.537a/s320x320/65560614_2744658635549340_7359127836914876416_n.jpg?_nc_cat=105&_nc_oc=AQloSPiV91iYytfUS3Y1BWEfGMfEXhrOerY1AfZRvJlVQdxGpR77M17w45yAM5qle_M&_nc_ht=scontent-gig2-1.xx&oh=a4b0833d9be5bb5c5c3a7620bc762741&oe=5DBD5B74


<img class="bl bm k" sr
c="https://scontent-gig2-1.xx.fbcdn.net/v/t1.0-0/cp0/e15/q65/c0.2.960.537a/s320x320/65383387_2731235873558283_4339440853421391872_n.jpg?_nc_cat=106&_nc_oc=AQkO-Mag6gkqNgQEElJNKFGNXJVIgsnw1sidTss2DvFHC4w43Y2vQpDy-oEsW1IknC8&_nc_ht=scontent-gig2-1.xx&oh=cb2dbf166cbdb38720eaa8e4a67cd20e&oe=5DAB86AA"/>


'''