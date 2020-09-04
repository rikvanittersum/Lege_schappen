from django.shortcuts import render
from .models import Supermarkt, Uitverkochte_product
import json
from django.core import serializers


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def supermarkten_view(request, *args, **kwargs):
    data = serializers.serialize('python', Supermarkt.objects.all())
    for d in data:
        d['fields']['pk'] = d['pk']

    objecten = [d['fields'] for d in data]

    for item in objecten:
        producten = serializers.serialize('python', Uitverkochte_product.objects.filter(supermarkt_id=item['pk']))
        item['uitverkochte_producten'] = [p['fields']['naam'] for p in producten]

    joe = json.dumps(objecten)
    context = {"supermarkten": joe}

    return render(request, 'supermarkten.html', context)


