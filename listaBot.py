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
        self.dateformatted = dateformatted
        self.locationName = locationName
        self.address = address
        self.img = img

def format_date(datefull):
    try:
        dtsplittedByComma = datefull.split(",")
        dtWithPrep = dtsplittedByComma[1].strip()
        dtsplittedByPrep = dtWithPrep.split("de")
        day = dtsplittedByPrep[0].strip()
        month = dtsplittedByPrep[1].strip()
        monthNumber = return_monthNumber(month)
        year = dtsplittedByPrep[2].strip()
        # Sábado, 6 de julho de 2019 de 20:00 a 05:00 UTC-03 vs Domingo, 14 de julho de 2019 às 17:00 UTC-03
        if "às" in year:
            yearSplitted = year.split("às")
            year = yearSplitted[0].strip()
            timeSplitted = yearSplitted[1].strip().split(" ")
            time =  timeSplitted[0]
        else:
            time = dtsplittedByPrep[3]
		# /fix inconsistência na data por extenso
        timeSplitted = time.split("a")
        timeSplitted2 = timeSplitted[0].strip().split(":")
        hour = timeSplitted2[0]
        minute = timeSplitted2[1]

        dateformatted = datetime.datetime(int(year), monthNumber, int(day), int(hour), int(minute), 00)
        return dateformatted
    except:
        return "ERROR"

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
'''
urList.append('https://m.facebook.com/pg/festacollegerock/events')
urList.append('https://m.facebook.com/heavydutybeerclub/pages/permalink/?view_type=tab_events')
urList.append('https://m.facebook.com/buffallosbar/pages/permalink/?view_type=tab_events')
urList.append('https://m.facebook.com/festailovethe90s/pages/permalink/?view_type=tab_events')
urList.append('https://m.facebook.com/pg/festarockaway/events/')
urList.append('https://m.facebook.com/saloon79/pages/permalink/?view_type=tab_events')
urList.append('https://m.facebook.com/pg/cariocaandroll/events')
urList.append('https://m.facebook.com/pg/gameoverpartybr/events')
urList.append('https://m.facebook.com/pg/festacrush/events/')
urList.append('https://m.facebook.com/pg/festatripoficial/events')
urList.append('https://m.facebook.com/TheRockBar.Rio/pages/permalink/?view_type=tab_events')
urList.append('https://m.facebook.com/calaboucobar/pages/permalink/?view_type=tab_events')
urList.append('https://m.facebook.com/pg/paranoidandroidparty/events')
'''

events = []

for url in urList:
	eventsList = requests.get(url)
	eventsListSourceCode = bs(eventsList.text, 'html.parser')
	if "permalink" in url:
		ClassInEventsListSourceCode = eventsListSourceCode.findAll("span", {"class": "br"})
	else:
		ClassInEventsListSourceCode = eventsListSourceCode.findAll("span", {"class": "bv"})

	eventPageList = []

	for Class in ClassInEventsListSourceCode:
		for a in Class.find_all('a', href=True):
			urlSplitted = a['href'].split('?')
			eventPageList.append(urlSplitted[0])  # /events/9999999999
		
	for event in eventPageList:
		eventId = event.replace('/events/', '')
		#verificar se o id evento já existe na lista
		eventUrl = 'https://m.facebook.com' + event
		eventPage = requests.get(eventUrl)
		eventPageSourceCode = bs(eventPage.text, 'html.parser')

		tagDD = eventPageSourceCode.find_all('dd')
		eventStreetAddress = str(tagDD[1].text)

		tagDT = eventPageSourceCode.find_all('dt')
		eventDateFull = str(tagDT[0].text)

		eventDateFormatted = format_date(eventDateFull)
		if eventDateFormatted == "ERROR":
			continue          #move to next iteration if can't format the event date

		eventLocationName = str(tagDT[1].text)
		tagBE = eventPageSourceCode.find("div", {"class": "be"})

		try:
			eventImgSrc = tagBE.find('img')['src']
		except:
			eventImgSrc = ''

		eventTitle = eventPageSourceCode.find('title').text

		#if (datetime.datetime.now() + datetime.timedelta(hours=-6)) < eventDateFormatted:
		if datetime.datetime.now() < eventDateFormatted:
			events.append(
				Event(eventId, eventUrl, eventTitle, eventDateFull, str(eventDateFormatted), eventLocationName, eventStreetAddress, eventImgSrc)
			)		

events.sort(key=lambda x: x.dateformatted, reverse=False)
json_string = json.dumps([ob.__dict__ for ob in events], indent=4)
updated_at = datetime.datetime.now()
print (json_string)
