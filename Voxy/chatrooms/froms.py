
from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Tapez votre message...'}))
