from django.db import models
from rooms.enum import RoomGenre
from uuid import uuid4


def generate_channel():
    new_channel = uuid4()
    if Rooms.objects.filter(channel=new_channel).exists():
        return generate_channel()
    return new_channel


class Rooms(models.Model):
    channel = models.UUIDField(unique=True, default=generate_channel)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    type = models.PositiveSmallIntegerField(choices=RoomGenre.to_choices())
