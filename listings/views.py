from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Band, Event
from .serializers import (
    ListingSerializer,
    BandSerializer,
    EventSerializer,
    EventDetailSerializer,
)

# Create your views here.


class BandViewSet(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
