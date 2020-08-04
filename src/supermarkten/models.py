from django.db import models
from django_mysql.models import ListTextField

# Create your models here.
class Supermarkt(models.Model):
    bedrijf                = models.TextField()
    adres                  = models.TextField()
    plaatsnaam             = models.TextField()
    uitverkochte_producten = ListTextField(base_field=models.CharField(max_length=100))


    def product_is_uitverkocht(self, product):
        if not product:
            raise ValueError("Geen product opgegeven")
        self.uitverkochte_producten.append(product)
        self.save()

    def product_is_niet_meer_uitverkocht(self, product):
        self.uitverkochte_producten.remove(product)


