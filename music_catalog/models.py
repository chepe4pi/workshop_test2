from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=127)
    style = models.CharField(max_length=127)
    year_born = models.IntegerField()


class Song(models.Model):
    artist = models.ForeignKey(Artist, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=127)
