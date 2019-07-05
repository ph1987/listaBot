'''
import requests
from bs4 import BeautifulSoup as bs
import json
import datetime

class Event:
    def __init__(self, id, url, title, datefull, dateformatted, locationName, address, img):
        self.id = id
        self.url = url
        self.title = title
        self.datefull = datefull
        self.dateformatted = str(format_date(dateformatted))
        self.locationName = locationName
        self.address = address
        self.img = img

def format_date(datefull):
    dtsplittedByComma = datefull.split(",")
    dtWithPrep = dtsplittedByComma[1].strip()
    dtsplittedByPrep = dtWithPrep.split("de")
    day = dtsplittedByPrep[0].strip()
    month = dtsplittedByPrep[1].strip()
    monthNumber = return_monthNumber(month)
    year = dtsplittedByPrep[2].strip()

    time = dtsplittedByPrep[3]
    timeSplitted = time.split("a")
    timeSplitted2 = timeSplitted[0].strip().split(":")
    hour = timeSplitted2[0]
    minute = timeSplitted2[1]

    dateformatted = datetime.datetime(int(year), monthNumber, int(day), int(hour), int(minute), 00)
    return dateformatted

def return_monthNumber(month):
    switcher = {
        "janeiro": 1,
        "fevereiro": 2,
        "março": 3,
        "abril": 4,
        "maio": 5,
        "junho": 6,
        "julho": 7,
        "agosto": 8,
        "setembro": 9,
        "outubro": 10,
        "novembro": 11,
        "dezembro": 12
    }
    return switcher.get(month, "Invalid month")

urList = []
urList.append('https://m.facebook.com/pg/casadamatriz/events')

for url in urList:
	eventsList = requests.get(url)
	eventsListSourceCode = bs(eventsList.text, 'html.parser')
	bvClassInEventsListSourceCode = eventsListSourceCode.findAll("span", {"class": "bv"})

	eventPageList = []
	events = []

	for bvClass in bvClassInEventsListSourceCode:
		for a in bvClass.find_all('a', href=True):
			urlSplitted = a['href'].split('?')
			eventPageList.append(urlSplitted[0])  # /events/9999999999
		
	for event in eventPageList:
		eventId = event.replace('/events/', '')
		eventUrl = 'https://m.facebook.com' + event
		eventPage = requests.get(eventUrl)
		eventPageSourceCode = bs(eventPage.text, 'html.parser')
		
		eventDateFullAndLocationName = eventPageSourceCode.findAll("div", {"class": "ct cu cg"})
		if not eventDateFullAndLocationName:
			#eventDateFullAndLocationName = eventPageSourceCode.findAll("div", {"class": "cq cr cd"})
			eventDateFullAndLocationName = eventPageSourceCode.find_all("div", class_=lambda value: value and value.startswith("cq cr cd"))
			
		eventTimeUntilAndStreetAddress = eventPageSourceCode.findAll("div", {"class": "cv cw cg"})
		if not eventTimeUntilAndStreetAddress:
			eventTimeUntilAndStreetAddress = eventPageSourceCode.findAll("div", {"class": "cs ct cd"})
			
		imgRaw = eventPageSourceCode.find("img", {"class": "bl bm k"})
		if imgRaw:
			imgSrcRaw = imgRaw['src']
		else:
			imgRaw = eventPageSourceCode.find("img", {"class": "bf k"})
			if imgRaw:
				imgSrcRaw = imgRaw['src']
			
		eventTitle = eventPageSourceCode.find('title').text
		
		if eventDateFullAndLocationName:
			if eventDateFullAndLocationName[0]:
				eventDateFull = eventDateFullAndLocationName[0].text
			else:
				eventDateFull = ''
			
			if eventDateFullAndLocationName[1]:
				eventLocationName = eventDateFullAndLocationName[1].text
			else:
				eventLocationName = ''
			
		if eventTimeUntilAndStreetAddress:
			#eventTimeUntilAndWeather = eventTimeUntilAndStreetAddress[0].text
			eventStreetAddress = eventTimeUntilAndStreetAddress[1].text
		else:
			eventStreetAddress = ''

		events.append(
			Event(eventId, eventUrl, eventTitle, eventDateFull, eventDateFull, eventLocationName, eventStreetAddress, imgSrcRaw)
		)

	json_string = json.dumps([ob.__dict__ for ob in events], indent=4)
	print (json_string)
'''
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

''' DEBUG MODE '''

import requests
from bs4 import BeautifulSoup as bs
import json
import datetime

class Event:
    def __init__(self, id, url, title, datefull, dateformatted, locationName, address, img):
        self.id = id
        self.url = url
        self.title = title
        self.datefull = datefull
        self.dateformatted = str(format_date(dateformatted))
        self.locationName = locationName
        self.address = address
        self.img = img

def format_date(datefull):
    dtsplittedByComma = datefull.split(",")
    dtWithPrep = dtsplittedByComma[1].strip()
    dtsplittedByPrep = dtWithPrep.split("de")
    day = dtsplittedByPrep[0].strip()
    month = dtsplittedByPrep[1].strip()
    monthNumber = return_monthNumber(month)
    year = dtsplittedByPrep[2].strip()

    time = dtsplittedByPrep[3]
    timeSplitted = time.split("a")
    timeSplitted2 = timeSplitted[0].strip().split(":")
    hour = timeSplitted2[0]
    minute = timeSplitted2[1]

    dateformatted = datetime.datetime(int(year), monthNumber, int(day), int(hour), int(minute), 00)
    return dateformatted

def return_monthNumber(month):
    switcher = {
        "janeiro": 1,
        "fevereiro": 2,
        "março": 3,
        "abril": 4,
        "maio": 5,
        "junho": 6,
        "julho": 7,
        "agosto": 8,
        "setembro": 9,
        "outubro": 10,
        "novembro": 11,
        "dezembro": 12
    }
    return switcher.get(month, "Invalid month")

urList = []
urList.append('https://m.facebook.com/pg/casadamatriz/events')

for url in urList:
	eventsList = requests.get(url)
	eventsListSourceCode = bs(eventsList.text, 'html.parser')
	bvClassInEventsListSourceCode = eventsListSourceCode.findAll("span", {"class": "bv"})

	eventPageList = []
	events = []

	event = '/events/413592285909653'
	eventId = event.replace('/events/', '')
	eventUrl = 'https://m.facebook.com' + event
	eventPage = requests.get(eventUrl)
	eventPageSourceCode = bs(eventPage.text, 'html.parser')
	
	#print(eventPageSourceCode)
	
	tagDD = eventPageSourceCode.find_all('dd')
	print('tagDD[0]: ' + str(tagDD[0].text))
	print('tagDD[1]: ' + str(tagDD[1].text))
	tagDT = eventPageSourceCode.find_all('dt')
	print('tagDT[0]: ' + str(tagDT[0].text))
	print('tagDT[1]: ' + str(tagDT[1].text))
	
	
	#img verificar class="be"
'''

eventDateFullAndLocationName = eventPageSourceCode.findAll("div", {"class": "ct cu cg"})
	if not eventDateFullAndLocationName:
		#eventDateFullAndLocationName = eventPageSourceCode.findAll("div", {"class": "cq cr cd"})
		eventDateFullAndLocationName = eventPageSourceCode.find_all("div", class_=lambda value: value and value.startswith("cq cr cd"))
		#print(eventDateFullAndLocationName)
		
	eventTimeUntilAndStreetAddress = eventPageSourceCode.findAll("div", {"class": "cv cw cg"})
	if not eventTimeUntilAndStreetAddress:
		eventTimeUntilAndStreetAddress = eventPageSourceCode.findAll("div", {"class": "cs ct cd"})
		
		
	imgRaw = eventPageSourceCode.find("img", {"class": "bl bm k"})
	if imgRaw:
		imgSrcRaw = imgRaw['src']
	else:
		imgRaw = eventPageSourceCode.find("img", {"class": "bf k"})
		if imgRaw:
			imgSrcRaw = imgRaw['src']
		
	eventTitle = eventPageSourceCode.find('title').text
	
	if eventDateFullAndLocationName:
		if eventDateFullAndLocationName[0]:
			eventDateFull = eventDateFullAndLocationName[0].text
			#print(eventDateFull)
		else:
			eventDateFull = ''
			#print(eventDateFull)
		
		if len(eventDateFullAndLocationName) >= 2:
			eventLocationName = eventDateFullAndLocationName[1].text
			#print(eventLocationName)
		else:
			eventLocationName = ''
			#print(eventLocationName)
	
	if eventTimeUntilAndStreetAddress:
		#eventTimeUntilAndWeather = eventTimeUntilAndStreetAddress[0].text
		eventStreetAddress = eventTimeUntilAndStreetAddress[1].text
		#print(eventStreetAddress)
	else:
		eventStreetAddress = ''
		
	print(eventDateFullAndLocationName)
	
	# pegar tags <dd> e <dt>
	
	
	events.append(
		Event(eventId, eventUrl, eventTitle, eventDateFull, eventDateFull, eventLocationName, eventStreetAddress, imgSrcRaw)
	)		

	json_string = json.dumps([ob.__dict__ for ob in events], indent=4)
	print (json_string)
'''