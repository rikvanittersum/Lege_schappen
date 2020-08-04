from django.test import TestCase
from .models import Supermarkt


class SupermarktTestCase(TestCase):
    def setUp(self):
        Supermarkt.objects.create(bedrijf="ah", adres="dreef", plaatsnaam="Amsterdam", uitverkochte_producten =[])

    def test_een_product_dat_is_uitverkocht_kan_worden_toegevoegd(self):
        supermarkt = Supermarkt.objects.get(bedrijf="ah")
        supermarkt.product_is_uitverkocht("salami")
        self.assertEqual(supermarkt.uitverkochte_producten[0], "salami")

    def test_een_product_dat_niet_meer_is_uitverkocht_kan_uit_de_lijst_worden_verwijderd(self):
        supermarkt = Supermarkt.objects.get(bedrijf="ah")
        supermarkt.product_is_uitverkocht("salami")
        supermarkt.product_is_niet_meer_uitverkocht("salami")
        self.assertListEqual(supermarkt.uitverkochte_producten, [])
