import json
import requests

urList = []
def all():
    with open('fbpages.json', 'r') as f:
        data = json.load(f)
        for e in data['events']:
            if (len(e['url']) > 0):
                urList.append(e['url'])

    return urList
def one():
    urList.append('https://m.facebook.com/pg/casadamatriz/events')
    return urList
    
def protected():
    urList.append('https://m.facebook.com/barbukowskirio/events')
    urList.append('https://m.facebook.com/fosfoboxbarclub/events')
    return urList


#urList.append('https://m.facebook.com/pg/casadamatriz/events')
#urList.append('https://m.facebook.com/saloon79/pages/permalink/?view_type=tab_events')
#urList.append('https://m.facebook.com/LaEsquinaTeatroBar/pages/permalink/?view_type=tab_events')
#urList.append('https://m.facebook.com/pg/gameoverpartybr/events')
#urList.append('https://m.facebook.com/pg/festacrush/events')
#urList.append('https://m.facebook.com/pg/festatripoficial/events')
#urList.append('https://m.facebook.com/TheRockBar.Rio/pages/permalink/?view_type=tab_events')
#urList.append('https://m.facebook.com/calaboucobar/pages/permalink/?view_type=tab_events')
#urList.append('https://m.facebook.com/pg/paranoidandroidparty/events')
#urList.append('https://m.facebook.com/boemiadalapa/pages/permalink/?view_type=tab_events')
#urList.append('https://m.facebook.com/Lapa-Irish-Pub-177596852262765/pages/permalink/?view_type=tab_events')
#urList.append('https://m.facebook.com/pg/macacocaolhopub/events')
#urList.append('https://m.facebook.com/SuburbioAlternativo/pages/permalink/?view_type=tab_events')
#urList.append('https://m.facebook.com/pg/duckwalkpub/events')
#urList.append('https://m.facebook.com/pg/BandaVenuz/events')
#urList.append('https://m.facebook.com/GatoNegroPub/pages/permalink/?view_type=tab_events')
#urList.append('https://m.facebook.com/brookspubrj/pages/permalink/?view_type=tab_events')
#urList.append('https://m.facebook.com/pg/festarockcetera/events')									#só aparece se tiver logado
#urList.append('https://m.facebook.com/festarockme/events/')										#só aparece se tiver logado
#urList.append('https://m.facebook.com/pg/pubpanqss/events')
#urList.append('https://m.facebook.com/rotarj65/pages/permalink/?view_type=tab_events')
#urList.append('https://m.facebook.com/barbukowskirio/events')      #só aparece se tiver logado