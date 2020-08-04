from django.db import models
from django_mysql.models import ListTextField

# Create your models here.
class Supermarkt(models.Model):
    bedrijf                = models.TextField()
    adres                  = models.TextField()
    plaatsnaam             = models.TextField()
    uitverkochte_producten = ListTextField(base_field=models.CharField(max_length=100))


    def set_uitverkochte_producten(self, product):
        self.uitverkochte_producten.append(product)
        self.save()


