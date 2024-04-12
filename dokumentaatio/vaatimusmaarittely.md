# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on Tetris peli, jossa tarkoituksena on kerätä pisteitä pudottamalla palikoita ja koota niistä vaakasuoria rivejä.
Kun pelaaja saa rivin valmiiksi, se poistuu ja sitä ylempänä olevat palikat putoavat yhden rivin alemmaksi.
Lisäksi pelaajan pisteet nousevat.
Peli nopeutuu hiljalleen pelin edetessä tasosta riippuen.
Peli päättyy kun uusi palikka ei enää mahdu putoamaan alaspäin.

## Suunnitellut toiminnallisuudet

- [ ] Sovelluksen avauduttua näytetään näyttö, jossa on painike "Aloita peli" ja suurin saatu pistemäärä
- [x] Näytöllä on 10x20 ruudukko.
- [x] Näytön yläreunasta alkaa putoamaan yksi palikka kerrallaan alaspäin.
- [x] Palikkaa voi liikutella ja pyöritellä nuolinäppäimillä.
- [x] Palikan putoamista voi nopeuttaa painamalla nuolinäppäintä alaspäin.
- [x] Kun palikka osuu näytön alareunaan tai toiseen palikkaan niin, ettei se enää voi liikkua alaspäin, putoaa seuraava palikka.
- [x] Kun kokonainen rivi on saatu valmiiksi, se häviää, pistemäärä lisääntyy, pelin nopeus kasvaa ja sen yläpuolella olevat palikat putoavat alaspäin yhden rivin.
- [x] Kun palikka osuu toiseen palikkaan niin, että se on ruudukon yläpuolella, peli päättyy.
- [ ] Ruudukon vieressä oikealla näytetään seuraavaksi putoava palikka ja tilastot: pistemäärä, taso, kokonaiseksi saadut rivit.
- [ ] Pelin päätyttyä näytetään näyttö, jossa on painike "Pelaa uudelleen" ja tulokset: pelistä saatu pistemäärä ja kokonaiseksi saadut rivit