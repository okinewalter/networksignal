from django.contrib import admin
from .models import  Network, Location, Signal, Topsearch
 
admin.site.register(Network)
admin.site.register(Location)
admin.site.register(Signal)
admin.site.register(Topsearch)

