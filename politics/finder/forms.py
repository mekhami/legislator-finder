from django import forms


class FinderForm(forms.Form):
    # Basic form stuff.
    zipcode = forms.IntegerField()

    def query_api(self):
        # query the sunlight API, create a context object to return
        return data
