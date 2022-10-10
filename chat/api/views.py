from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.sessions.models import Session
from hashlib import md5


class HomeView(GenericViewSet):
    def create(self, request: Request, *args, **kwargs):
        sessionid = request.COOKIES.get('sessionid', '')
        if not sessionid:
            return Response(status=401)
        session: Session = Session.objects.get(pk=sessionid)
        if session is None:
            return Response(status=401)
        user_name = session.get_decoded()['name']
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"chat_{md5(request.data['room'].encode()).hexdigest()}", {
                'type': 'chat_message',
                'message': request.data['message'],
                'name': user_name
            })
        return Response()
