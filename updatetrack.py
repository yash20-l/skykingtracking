from distutils.log import error
import requests



def trackEveryShipment():

    data = requests.get('http://localhost:8000/getships')
    dataJson = data.json()
    for ships in dataJson:
        tcode = ships['fields']['tcode']
        url = f'https://live.skyking.co/api/Track/ConsignmentMTrack_WebSite_AuthNew?cnote={tcode}&key=skm&email=skm@flyking.co.in'
        headers = {
            "KeyValue": "wdFm5gZ7Wyh9aLvxcPU5Q1k5vhL/9K0g01d2H4JmJRR8+7VhRoucbv/SkTkRrXnk5R7PJkXm+ZoEtaXaR0Ci+MZ/gCektrIgalRYsorAspNDDISVSsm9qtJtfEraDbwf",
            "Content-Type": "application/json"
        }
        res = requests.get(url, headers=headers)
        status = res.json()
        if(len(status) == 0):
            qstatus = 'booked'
        else:
            qstatus = status[-1]['Status']
        requests.get('http://localhost:8000/updateships', {
            'tcode' : tcode,
            'status' : qstatus
        })
        

trackEveryShipment()
