from django import forms


class ZipForm(forms.Form):
    # Basic form stuff.
    zipcode = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'zip-field form-control', 
                                                               'placeholder': 'Enter your Zip Code'}))
