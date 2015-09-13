from django.contrib import admin

from .models import Legislator, Vote, Bill

# Register your models here.
admin.site.register(Legislator)
admin.site.register(Bill)
admin.site.register(Vote)
