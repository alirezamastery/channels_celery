from django import forms


class ChatMessageForm(forms.Form):
    message = forms.CharField()