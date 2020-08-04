from django.shortcuts import render
from .models import Supermarkt

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def supermarkten_view(request, *args, **kwargs):
    supermarkten = Supermarkt.objects.all()
    supermarkten[0].voeg_uitverkocht_product_toe("henk")
    context = {"supermarkten" : supermarkten}
    return render(request, 'supermarkten.html', context)