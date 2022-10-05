from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from rooms.models import Rooms
from uuid import UUID


def index(request: WSGIRequest):
    channel = request.GET.get('channel', '')
    if not request.session.get('name', ''):
        return redirect('main')
    elif not channel or not Rooms.objects.filter(channel=UUID(channel)).exists():
        return redirect('rooms')

    return render(
        request,
        'chat/base.html', {
            'channel': channel
        }
    )
