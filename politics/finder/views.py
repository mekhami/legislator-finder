from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from .forms import FinderForm

# Create your views here.
class IndexView(FormView):
    form_class = FinderForm

    def form_valid(self, form):
        # perform the API request
        legislators = form.query_api()
        pass

def index_view(request):
    return render(request, 'finder/index.html')

def zipcode_view(request):
    if request.method == "POST":
        # perform the API request, create the context object from the representatives
        # context = ?
        return render(request, 'finder/results.html', context)
    else:
        return HttpResponseRedirect('/')
