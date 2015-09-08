from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import FinderForm
from .api import query_api

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'finder/index.html')

    def post(self, request, *args, **kwargs):
        return redirect('zip-detail', zipcode=request.POST['zipcode'])

class ZipCodeView(View):
    def get(self, request, *args, **kwargs):
        legislators = query_api(kwargs['zipcode'])
        return render(request, 'finder/zip_detail.html', {'legislators': legislators})
