from django.test import TestCase
from .models import Supermarkt
from .views import meeste_producten


class SupermarktTestCase(TestCase):
    def setUp(self):
        Supermarkt.objects.create(bedrijf="ah", adres="dreef", plaatsnaam="Amsterdam", uitverkochte_producten =[])
        Supermarkt.objects.create(bedrijf="dirk", adres="dreef", plaatsnaam="Amsterdam", uitverkochte_producten=["joe"])
        Supermarkt.objects.create(bedrijf="c1000", adres="dreef", plaatsnaam="Amsterdam", uitverkochte_producten=["joe", "nog een"])

    def test_een_product_dat_is_uitverkocht_kan_worden_toegevoegd(self):
        supermarkt = Supermarkt.objects.get(bedrijf="ah")
        supermarkt.product_is_uitverkocht("salami")
        self.assertEqual(supermarkt.uitverkochte_producten[0], "salami")

    def test_als_geen_product_wordt_meegeleverd_bij_uitverkocht_product_levert_dat_een_value_error_op(self):
        supermarkt = Supermarkt.objects.get(bedrijf="ah")
        self.assertRaises(ValueError, supermarkt.product_is_uitverkocht, "")

    def test_een_product_dat_niet_meer_is_uitverkocht_kan_uit_de_lijst_worden_verwijderd(self):
        supermarkt = Supermarkt.objects.get(bedrijf="ah")
        supermarkt.product_is_uitverkocht("salami")
        supermarkt.product_is_niet_meer_uitverkocht("salami")
        self.assertListEqual(supermarkt.uitverkochte_producten, [])

    def test_als_geen_product_wordt_meegeleverd_bij_een_niet_meer_uitverkocht_product_levert_dat_een_value_error_op(self):
        supermarkt = Supermarkt.objects.get(bedrijf="ah")
        self.assertRaises(ValueError, supermarkt.product_is_niet_meer_uitverkocht, "")

    def test_krijg_supermarkt_met_meest_uitverkochte_producten(self):
        supermarkt_met_meest_uitverkochte_producten = meeste_producten(Supermarkt.objects.all())
        self.assertEqual(supermarkt_met_meest_uitverkochte_producten, "c1000")



