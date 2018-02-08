from django.shortcuts import render_to_response
from rest_framework.viewsets import ModelViewSet

from music_catalog.models import Song
from music_catalog.serializers import SongSerializer


def main_view(request):
    songs = Song.objects.all()
    return render_to_response('main_template.html', context={'songs': songs})


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
