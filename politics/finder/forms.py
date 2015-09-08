from django import forms


class ZipForm(forms.Form):
    # Basic form stuff.
    zipcode = forms.IntegerField()
