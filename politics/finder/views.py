from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import ZipForm
from .api import query_api, legislator_committees
from .models import Legislator

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
        for leg in legislators:
            db_leg = Legislator.objects.get(bioguide_id=leg['bioguide_id'])
            leg['image_url'] = db_leg.congress_image_url
            leg['votes'] = db_leg.vote_set.all()
            leg['committees'] = legislator_committees(leg['bioguide_id'])
        return render(request, 'finder/zip_detail.html', {'legislators': legislators})
