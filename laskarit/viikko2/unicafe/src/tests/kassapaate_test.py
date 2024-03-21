import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_rahamaara_ja_myytyjen_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_kassassa_oleva_raha_kasvaa_ja_vaihtorahan_suuruus(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1006.4)

    def test_myytyjen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 1)

        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maksu_ei_riittava_summa_ei_muutu_rahat_palautetaan_myyty_lounas_ei_kasva(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(1), 1)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1), 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_korttiosto_veloitetaan_summa_ja_palautetaan_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_korttiosto_myytyjen_lounaiden_maara_kasvaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.edulliset, 1)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_ei_tarpeeksi_rahaa(self):
        self.maksukortti = Maksukortti(100)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

        self.assertEqual(self.maksukortti.saldo_euroina(), 1)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_kassa_rahamaara_kasvaa_ladatulla_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002)
        self.assertEqual(self.maksukortti.saldo_euroina(), 12)

    def test_lataa_negatiivinen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)