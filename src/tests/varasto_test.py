import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.tyhja = Varasto(0,-10)
        self.tilavuus_pienempi = Varasto(5,10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_tilavuus_nollataan(self):
        self.assertAlmostEqual(self.tyhja.tilavuus, 0)

    def test_alkusaldo_minimissään_nolla(self):
        self.assertAlmostEqual(self.tyhja.saldo, 0)

    def test_tilavuus_pienempi_kuin_saldo(self):
        self.assertAlmostEqual(self.tilavuus_pienempi.saldo, self.tilavuus_pienempi.tilavuus)

    def test_varastoon_lisataan_negatiivinen(self):
        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varastoon_lisataan_liikaa(self):
        self.varasto.lisaa_varastoon(20)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_varastosta_otetaan_negatiivinen_summa(self):
        self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_varastosta_otetaan_enemman_kuin_sallitaan(self):
        self.varasto.ota_varastosta(50)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_kortti_tulostaa_oikein(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
        