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


class EventDetailSerializer(serializers.ModelSerializer):
    band = BandSerializer()
    listings = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = "__all__"

    def get_listings(self, obj):
        # Filter listings related to the current event (obj)
        listings = Listing.objects.filter(event=obj)
        return ListingSerializer(listings, many=True).data
