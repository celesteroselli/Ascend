from django import forms
from .models import *

class MessageForm(forms.ModelForm):
    video = forms.FileInput()
    content = forms.CharField(required=False)

    class Meta:
        model = Message
        exclude = ("msg_from","msg_to",)