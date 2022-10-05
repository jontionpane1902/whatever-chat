from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest


def index(request: WSGIRequest):
    if request.session.get('name', ''):
        return redirect('rooms')

    if request.method == 'POST':
        request.session.create()
        name = request.POST.get('username', '')
        request.session['name'] = name
        return redirect('rooms')

    return render(request, 'main/base.html')
