from django.test import TestCase
from .models import Supermarkt


class SupermarktTestCase(TestCase):
    def setUp(self):
        Supermarkt.objects.create(bedrijf="ah", adres="dreef", plaatsnaam="Amsterdam", uitverkochte_producten =[])

    def test_een_product_dat_is_uitverkocht_kan_worden_toegevoegd(self):
        supermarkt = Supermarkt.objects.get(bedrijf="ah")
        supermarkt.set_uitverkochte_producten("salami")
        self.assertEqual(supermarkt.uitverkochte_producten[0], "salami")
