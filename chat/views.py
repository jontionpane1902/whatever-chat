from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from rooms.models import Rooms
from uuid import UUID


def index(request: WSGIRequest):
    channel = request.GET.get('channel', '')
    if not request.session.get('name', ''):
        return redirect('main')
    room: Rooms = Rooms.objects.filter(channel=UUID(channel)).first()
    if not channel or room is None:
        return redirect('rooms')

    return render(
        request,
        'chat/base.html', {
            'channel': channel,
            'room_name': room.name,
        }
    )
