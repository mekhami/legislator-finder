from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import ZipForm
from .api import query_api

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = ZipForm()
        return render(request, 'finder/index.html', {'form': form})

    def post(self, request, *args, **kwargs):
        return redirect('zip-detail', zipcode=request.POST['zipcode'])

class ZipCodeView(View):
    def get(self, request, *args, **kwargs):
        legislators = query_api(kwargs['zipcode'])
        return render(request, 'finder/zip_detail.html', {'legislators': legislators})
