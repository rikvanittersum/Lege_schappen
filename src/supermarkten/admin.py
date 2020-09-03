from django.contrib import admin

# Register your models here.
from .models import Supermarkt, Uitverkochte_product

admin.site.register(Supermarkt)
admin.site.register(Uitverkochte_product)