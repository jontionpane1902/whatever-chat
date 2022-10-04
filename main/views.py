from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest


def index(request: WSGIRequest):
    if request.session.session_key:
        return redirect('rooms')
    request.session.create()
    if request.method == 'POST':
        name = request.POST.get('username', '')
        request.session['name'] = name
    return render(request, 'main/base.html')
