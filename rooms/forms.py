from django.forms import ModelForm
from .models import Rooms


class RoomsForm(ModelForm):
    class Meta:
        model = Rooms
        exclude = ('id', 'channel')
