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
	imgSrcRaw = eventPageSourceCode.find("img", {"class": "bl bm k"})['src']
	eventTitle = eventPageSourceCode.find('title').text

	eventDateFull = eventDateFullAndLocationName[0].text
	eventLocationName = eventDateFullAndLocationName[1].text
	eventTimeUntilAndWeather = eventTimeUntilAndStreetAddress[0].text
	eventStreetAddress = eventTimeUntilAndStreetAddress[1].text
	
	print("url:" + eventUrl)
	print("title: " + eventTitle)
	print("date: " + eventDateFull)
	print("host: " + eventLocationName)
	print("time remaining: " + eventTimeUntilAndWeather)
	print("address: " + eventStreetAddress)
	print("img: \n" + imgSrcRaw)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-