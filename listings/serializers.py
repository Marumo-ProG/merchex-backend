from rest_framework import serializers
from .models import Listing, Band, Event


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"
