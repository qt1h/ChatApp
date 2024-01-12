
from django import forms
from manage_emojis.models import Emoji

class MessageForm(forms.Form):
    message = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Tapez votre message...'}))
    emoji = forms.ModelChoiceField(queryset=Emoji.objects.all(), empty_label=None)