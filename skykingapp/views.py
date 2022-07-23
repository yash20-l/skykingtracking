from ast import Try
from time import time
from django.http import HttpResponse, JsonResponse
import datetime
import requests
from .models import Tracking
from django.shortcuts import redirect, render
from django.core import serializers

def index(request):
    allshipments = Tracking.objects.all()
    delivered = 0
    revship = list(reversed(allshipments))[:10]
    for ships in allshipments:
        if ships.status.find('Delivered') != -1:
            delivered = delivered + 1
        elif ships.status.find('Out For Delivery') != -1:
            delivered = delivered + 1
    return render(request, 'dashboard.html', {
        "shipments" : allshipments,
        "delivered" : delivered,
        "revship" : revship
    })


def trackShipment(tcode):
    url = f'https://live.skyking.co/api/Track/ConsignmentMTrack_WebSite_AuthNew?cnote={tcode}&key=skm&email=skm@flyking.co.in'
    headers = {
        "KeyValue": "wdFm5gZ7Wyh9aLvxcPU5Q1k5vhL/9K0g01d2H4JmJRR8+7VhRoucbv/SkTkRrXnk5R7PJkXm+ZoEtaXaR0Ci+MZ/gCektrIgalRYsorAspNDDISVSsm9qtJtfEraDbwf",
        "Content-Type": "application/json"
    }
    res = requests.get(url, headers=headers)
    return res.json()


def numConcat(num1, num2):

    # Convert both the numbers to
    # strings
    num1 = str(num1)
    num2 = str(num2)

    # Concatenate the strings
    num1 += num2

    return int(num1)


def track(request):
    tcode = request.GET.get('tcode')
    details = trackShipment(tcode=tcode)
    return render(request, 'tracking.html', {"details": details})



def addTrack(request):
    if request.method == 'POST':
        mainseries = request.POST.get('mainseries')
        starting = int(request.POST.get('starting'))
        ending = int(request.POST.get('ending'))

        try:
            for num in range(starting, ending + 1):
                tcode = numConcat(mainseries, num)
                savetrack = Tracking(tcode=tcode)
                savetrack.save()
        except:
            print('error occured')
            return render(request, '404.html')



    return render(request, 'addtrack.html')

def getShipments(request):
    shipments = Tracking.objects.all()
    shipsJs = serializers.serialize('json', shipments)
    return HttpResponse(shipsJs, content_type='application/json')


def updateShips(request):
    tcode = request.GET.get('tcode')
    status = request.GET.get('status')
    tobj = Tracking.objects.get(tcode=tcode)
    tobj.status = status
    tobj.save()
    
    return JsonResponse({
        "status" : 200,
        "message" : "ok"
    })

def allships(request):
    ships = reversed(Tracking.objects.all())
    return render(request, 'viewships.html', {
        "ships" : ships
    })