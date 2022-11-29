
from django.urls import path
from .views import index, about, faq, contact, signal, getlocation, gettopsearch

urlpatterns = [
    path('', index, name ='home'),
    path('signal/', signal, name ='signal'),
    path('about/', about, name ='about'),
    path('faq/', faq, name ='faq'),
    path('contact/', contact, name ='contact'),
    path('getlocation/', getlocation, name ='getlocation'),
    path('gettopsearch/', gettopsearch, name ='gettopsearch'),
   
]
