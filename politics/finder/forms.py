from django import forms


class FinderForm(forms.Form):
    # Basic form stuff.
    zipcode = forms.IntegerField(min_length=5, max_length=5)

    def query_api(self):
        # query the sunlight API, create a context object to return
        return data
