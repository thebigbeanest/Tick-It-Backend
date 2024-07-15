from rest_framework import serializers
from .models import Venue, Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True
    )

    venue_id = serializers.PrimaryKeyRelatedField(
        queryset = Venue.objects.all(),
        source='venue'
    )

    class Meta:
        model = Event
        fields = ('id', 'venue', 'venue_id', 'name', 'start_time', 'end_time', 'date', 'price', 'details', 'image_url')
        
        
class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = EventSerializer(
        # view_name='Event_detail',
        many=True,
        read_only=True
    )

    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue_detail'
    )

    class Meta:
       model = Venue
       fields = ('id', 'venue_url', 'name', 'location', 'image_url', 'capacity', 
       'type', 'details', 'events')