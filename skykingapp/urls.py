
from django.urls import path
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index),
    path('track', views.track),
    path('addtrack', views.addTrack),
    path('getships', views.getShipments),
    path('updateships', views.updateShips),
    path('viewships', views.allships)
]
