import requests
from bs4 import BeautifulSoup as bs
import json
import datetime
import time
import formatdate
import urlist

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

urList = urlist.all()

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
			eventPageList.append(urlSplitted[0])
		
	for event in eventPageList:
		eventId = event.replace('/events/', '')
		eventUrl = 'https://m.facebook.com' + event
		eventPage = requests.get(eventUrl)
		eventPageSourceCode = bs(eventPage.text, 'html.parser')

		tagDD = eventPageSourceCode.find_all('dd')
		eventStreetAddress = str(tagDD[1].text)

		tagDT = eventPageSourceCode.find_all('dt')
		eventDateFull = str(tagDT[0].text)

		eventDateFormatted = formatdate.format_date(eventDateFull)
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
