from django.shortcuts import render
from django.db.models import Avg
from .forms import signalForm
from .models import Signal, Topsearch, Location
from django.views.decorators.http import   require_http_methods
from django.shortcuts import get_object_or_404

def index(request):    
    context = {}
    return render(request, 'gsm/index.html', context)


def signal(request):   
    context = {'form': signalForm()}
    return render(request, 'gsm/signal.html', context)

@require_http_methods(['POST'])
def gettopsearch(request):
    topsearch = Topsearch.objects.all().order_by('id')[:5]
    if topsearch:
        return render(request, 'gsm/topsearch.html', {'topsearch': topsearch})
    else:
        return render(request, 'gsm/topsearch.html', {'topsearch': ''})

def about(request):
    return render(request, 'gsm/about.html')

def faq(request):
    return render(request, 'gsm/faq.html')

def contact(request):
    return render(request, 'gsm/contact.html')

@require_http_methods(['POST'])
def getlocation(request):
    userlocation = request.POST.get('location', '')  or redirect(URL('getlocation'))   
    query = Signal.objects.values('network__name').filter(location=userlocation).annotate(rating=Avg('value')).order_by('rating')


    if query:
        try:
            top_search_query = Topsearch.objects.get(location=userlocation)
            top_search_query.counter += 1
            top_search_query.save()
        except:
            location = Location.objects.get(pk=userlocation)
            top_search_query = Topsearch(location=location, counter=1)
            top_search_query.save()






    return render(request, 'gsm/search.html', {'data': query})

