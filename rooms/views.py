from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from rooms.forms import RoomsForm
from rooms.models import Rooms


def index(request: WSGIRequest):
    if not request.session.get('name', ''):
        return redirect('main')
    room_list = Rooms.objects.all()
    room_form = RoomsForm(request.POST or None, request.FILES or None)
    if 'searchRoom' in request.GET:
        room_list = room_list.filter(
            name__icontains=request.GET['searchRoom'])
    if room_form.is_valid():
        room_form.save()

    return render(
        request,
        'rooms/base.html', {
            'room_list': room_list,
            'room_form': room_form
        }
    )
