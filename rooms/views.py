from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest


def index(request: WSGIRequest):
    if not request.session.session_key:
        return redirect('main')
    # TODO: Fetch room list
    return render(request, 'rooms/base.html')
