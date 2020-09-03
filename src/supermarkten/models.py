from django.db import models

class Supermarkt(models.Model):
    supermarkt_id          = models.AutoField(primary_key=True, serialize=True)
    bedrijf                = models.TextField()
    adres                  = models.TextField()
    plaatsnaam             = models.TextField()


class Uitverkochte_product(models.Model):
    naam          = models.TextField()
    supermarkt_id = models.IntegerField()
    datum         = models.DateTimeField()




