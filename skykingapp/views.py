from django.http import HttpResponse
import datetime
import requests
from django.shortcuts import redirect, render

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'dashboard.html')

def trackShipment(tcode):
    url = f'https://live.skyking.co/api/Track/ConsignmentMTrack_WebSite_AuthNew?cnote={tcode}&key=skm&email=skm@flyking.co.in'
    headers = {
        "KeyValue" : "wdFm5gZ7Wyh9aLvxcPU5Q1k5vhL/9K0g01d2H4JmJRR8+7VhRoucbv/SkTkRrXnk5R7PJkXm+ZoEtaXaR0Ci+MZ/gCektrIgalRYsorAspNDDISVSsm9qtJtfEraDbwf",
        "Content-Type" : "application/json"
    }
    res = requests.get(url, headers=headers)
    return res.json()

def track(request):
    if request.method == 'POST':
        tcode = request.POST.get('tcode')
        details = trackShipment(tcode=tcode)
        return render(request, 'tracking.html', {"details" : details})
    else:
        return redirect('/')
