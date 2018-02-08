from rest_framework import serializers

from music_catalog.models import Song


class SongSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name')

    class Meta:
        model = Song
        fields = ('artist_name', 'name')
