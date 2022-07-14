from django import forms


class LinkShorteningForm(forms.Form):
    long_url = forms.URLField()
