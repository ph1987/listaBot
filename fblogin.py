# src: https://gist.github.com/UndergroundLabs/fad38205068ffb904685
from bs4 import BeautifulSoup as bs
import requests
import urlist
USERNAME = 'dickvigarista888@gmail.com'
PASSWORD = 'paocomovo1'
PROTECTED_URL = 'https://m.facebook.com/barbukowskirio/events'
PROTECTED_URL2 = 'https://m.facebook.com/fosfoboxbarclub/events'
PROTECTED_URL3 = 'https://m.facebook.com/casadamatriz/events/'

def auth(session, email, password):
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)
    return response.cookies

def login():
    session = requests.session()
    cookies = auth(session, USERNAME, PASSWORD)
    return cookies, session

cookie, s = login()

urList = urlist.all()
for url in urList:
    response = s.get(url, cookies=cookie, allow_redirects=False)
    rText = bs(response.text, 'html.parser')
    eventsInHref = rText.select("a[href*=events]")
    eventPageList = []

    for a in eventsInHref:
        urlSplitted = a['href'].split('?')
        if ("/feed/watch" not in urlSplitted[0] and "/events/" in urlSplitted[0]):
            eventPageList.append(urlSplitted[0])  # /events/9999999999
            print(urlSplitted[0])

#print(cookie)