from django.shortcuts import render
from .models import Supermarkt
import json
from django.core import serializers

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def supermarkten_view(request, *args, **kwargs):
    data = serializers.serialize('python', Supermarkt.objects.all())
    objecten = [d['fields'] for d in data]
    joe = json.dumps(objecten)
    context = {"supermarkten": joe}
    return render(request, 'supermarkten.html', context)