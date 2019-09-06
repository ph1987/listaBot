import requests
from bs4 import BeautifulSoup as bs
import json
import datetime
import formatdate
import urlist
import unicodedata

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
			eventPageList.append(urlSplitted[0])  # /events/9999999999
		
	for event in eventPageList:
		eventId = event.replace('/events/', '')
		#verificar se o id evento já existe na lista
		eventUrl = 'https://m.facebook.com' + event
		eventPage = requests.get(eventUrl)
		eventPageSourceCode = bs(eventPage.text, 'html.parser')

		tagDD = eventPageSourceCode.find_all('dd')

		try:
			eventStreetAddress = str(tagDD[1].text)
		except:
			eventStreetAddress = ''

		tagDT = eventPageSourceCode.find_all('dt')

		try:
			eventDateFull = str(tagDT[0].text)
		except:
			eventDateFull = ''

		eventDateFormatted = formatdate.format_date(eventDateFull)
		if eventDateFormatted == "ERROR":
			continue          #move to next iteration if can't format the event date

		try:
			eventLocationName = str(tagDT[1].text)
		except:
			eventLocationName = ''
			
		tagBE = eventPageSourceCode.find("div", {"class": "be"})

		try:
			eventImgSrc = tagBE.find('img')['src']
		except:
			eventImgSrc = ''

		eventTitle = eventPageSourceCode.find('title').text

        #if datetime.datetime.now() < eventDateFormatted:
		if (datetime.datetime.now() + datetime.timedelta(hours=-6)) < eventDateFormatted:
			events.append(
				Event(eventId, eventUrl, eventTitle, eventDateFull, str(eventDateFormatted), eventLocationName, eventStreetAddress, eventImgSrc)
			)	
			print(eventTitle + " added")	

events.sort(key=lambda x: x.dateformatted, reverse=False)
json_string = json.dumps([ob.__dict__ for ob in events], indent=4)
updated_at = datetime.datetime.now()

parsed = json.loads(json_string)
with open('events.json', 'w', encoding="utf-8") as outfile:
	json.dump([ob.__dict__ for ob in events], outfile, indent=4, ensure_ascii=False)


#print (json_string)
