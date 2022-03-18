from requests import Request, Session
import json
import time
import webbrowser
import pprint


def getInfo (): # Function to get the info

    mathlen = int(input("Input length:"))
    
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = { 'slug': 'bitcoin', 'convert': 'USD' } 

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'YOUR KEYYYYYYYYYY!!!!!!!!!!!!!!'
    } 

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)

    info = json.loads(response.text)['data']['1']['quote']['USD']['percent_change_1h']
    info1 = json.loads(response.text)['data']['1']['quote']['USD']['price']
    info2 = json.loads(response.text)['data']['1']['quote']['USD']['percent_change_7d']
  
    math = info1*info2*info
    
    if math < 0:
        mathpostive=math*-1
    txt = str(mathpostive)
    tail, head, sap = txt.partition(".")
    mathstr = sap
 
    mathlen1 = mathstr[:mathlen]
  
    
    getInfo.mathfinal = info1
    print("This is your rundom number:",mathlen1)
    
    
    
    '''
    print("[D2]Price:",info1)
    print("[D1]Price change 1h:",info)
    print("[D3]Price chnage 7d:",info2)
    '''
    
    
    
getInfo() 



print("BTC price:",getInfo.mathfinal)



