from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.
def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='cricket')
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='cricket')
    QSW=Webpage.objects.exclude(topic_name='cricket')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.order_by('name')
    QSW=Webpage.objects.order_by('-name')
    QSW=Webpage.objects.order_by(Length('name'))
    QSW=Webpage.objects.filter(topic_name='kabbaddi').order_by('-name')
    QSW=Webpage.objects.order_by(Length('name').desc())
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.all().order_by('date')
    d={'accessrecords':QSA}
    return render(request,'display_accessrecords.html',d)