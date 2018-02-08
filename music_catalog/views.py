from django.shortcuts import render_to_response

from music_catalog.models import Song


def main_view(request):
    songs = Song.objects.all()
    return render_to_response('main_template.html', context={'songs': songs})
