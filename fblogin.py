# src: https://gist.github.com/UndergroundLabs/fad38205068ffb904685
import requests

PROTECTED_URL = 'https://m.facebook.com/barbukowskirio/events'
#PROTECTED_URL2 = 'https://m.facebook.com/fosfoboxbarclub/events'

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
response = s.get(PROTECTED_URL, cookies=cookie, allow_redirects=False)
print(response.text)