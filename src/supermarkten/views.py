from django.shortcuts import render
from .models import Supermarkt
import json
from django.core import serializers
from django.db.models import Max

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def supermarkten_view(request, *args, **kwargs):
    data = serializers.serialize('python', Supermarkt.objects.all())
    objecten = [d['fields'] for d in data]
    joe = json.dumps(objecten)
    max = meeste_producten(Supermarkt.objects.all())
    print(max)
    context = {"supermarkten": joe, "max": max}
    return render(request, 'supermarkten.html', context)

def meeste_producten(supermarkten):
    max_prod = 0
    ssuper = ""
    for supermarkt in supermarkten:
        if len(supermarkt.uitverkochte_producten) > max_prod:
            max_prod = len(supermarkt.uitverkochte_producten)
            ssuper = supermarkt.bedrijf

    return ssuper

