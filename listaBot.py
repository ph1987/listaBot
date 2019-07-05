import requests
from bs4 import BeautifulSoup as bs
import json

class Event:
    def __init__(self, id, url, title, datefull, dateformatted, locationName, address, img):
        self.id = id
        self.url = url
        self.title = title
        self.datefull = datefull
        self.dateformatted = format_date(dateformatted)
        self.locationName = locationName
        self.address = address
        self.img = img

def format_date(datefull):
    dtsplittedByComma = datefull.split(",")
    dtWithPrep = dtsplittedByComma[1].strip()
    dtsplittedByPrep = dtWithPrep.split("de")
    day = dtsplittedByPrep[0].strip()
    month = dtsplittedByPrep[1].strip()
    year = dtsplittedByPrep[2].strip()

    time = dtsplittedByPrep[3]
    timeSplitted = time.split("a")
    timeFormatted = timeSplitted[0].strip() + ":00"

    dateformatted = day + "/" + month + "/" + year + " " + timeFormatted
    return dateformatted

urList = []
urList.append('https://m.facebook.com/pg/casadamatriz/events')

for url in urList:
	eventsList = requests.get(url)
	eventsListSourceCode = bs(eventsList.text, 'html.parser')
	bvClassInEventsListSourceCode = eventsListSourceCode.findAll("span", {"class": "bv"})

	eventLPageList = []
	events = []

	for bvClass in bvClassInEventsListSourceCode:
		for a in bvClass.find_all('a', href=True):
			urlSplitted = a['href'].split('?')
			eventLPageList.append(urlSplitted[0])  # /events/9999999999

    
	eventId = eventLPageList[0].replace('/events/', '')
	eventUrl = 'https://m.facebook.com' + eventLPageList[0]
	eventPage = requests.get(eventUrl)
	eventPageSourceCode = bs(eventPage.text, 'html.parser')

	eventDateFullAndLocationName = eventPageSourceCode.findAll("div", {"class": "ct cu cg"})
	eventTimeUntilAndStreetAddress = eventPageSourceCode.findAll("div", {"class": "cv cw cg"})
	imgSrcRaw = eventPageSourceCode.find("img", {"class": "bl bm k"})['src']
	eventTitle = eventPageSourceCode.find('title').text

	eventDateFull = eventDateFullAndLocationName[0].text
	eventLocationName = eventDateFullAndLocationName[1].text
	#eventTimeUntilAndWeather = eventTimeUntilAndStreetAddress[0].text
	eventStreetAddress = eventTimeUntilAndStreetAddress[1].text

	events.append(
		Event(eventId, eventUrl, eventTitle, eventDateFull, eventDateFull, eventLocationName, eventStreetAddress, imgSrcRaw)
	)

	json_string = json.dumps([ob.__dict__ for ob in events], indent=4)
	print (json_string)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
