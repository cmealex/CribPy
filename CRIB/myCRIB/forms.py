from django import forms

from .models import Rooms


class RoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ('room', 'furniture', 'drawer_section', 'item_name', 'item_description', 'item_count', 'comments')