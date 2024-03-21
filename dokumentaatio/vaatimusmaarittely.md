# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on Tetris peli, jossa tarkoituksena on kerätä pisteitä pudottamalla palikoita ja koota niistä vaakasuoria rivejä.
Kun pelaaja saa rivin valmiiksi, se poistuu ja sitä ylempänä olevat palikat putoavat yhden rivin alemmaksi.
Lisäksi pelaajan pisteet nousevat.
Peli nopeutuu hiljalleen pelin edetessä tasosta riippuen.
Peli päättyy kun uusi palikka ei enää mahdu putoamaan alaspäin.

## Suunnitellut toiminnallisuudet

### Pelivalikko
Pelin aloitus näyttö, jossa on kolme painiketta: "Aloita peli", "Vaikeustaso" ja "Lopeta".
Ensimmäinen painike aloittaa uuden pelin.
Toinen painike muuttaa pelin vaikeustasoa (palikoiden putoamisnopeutta).
Kolmas painike lopettaa ja sulkee sovelluksen.
Lisäksi näytöllä lukee käyttäjän saama suurin pistemäärä.

### Peli
Näytöllä on 10x20 ruudukko.
Näytön yläreunasta alkaa putoamaan yksi palikka kerrallaan alaspäin.
Palikkaa voi pyöritellä nuolinäppäimillä.
Palikan putoamista voi nopeuttaa painamalla nuolinäppäintä alaspäin.
Kun palikka osuu näytön alareunaan tai toiseen palikkaan niin, ettei se enää voi liikkua alaspäin, putoaa seuraava palikka.
Kun kokonainen rivi on saatu valmiiksi, se häviää, pistemäärä lisääntyy, pelin nopeus kasvaa ja sen yläpuolella olevat palikat putoavat alaspäin yhden rivin.
Kun palikka osuu toiseen palikkaan niin, että se on ruudukon yläpuolella, peli päättyy.
Ruudukon vieressä oikealla näytetään seuraavaksi putoava palikka ja tilastot: pistemäärä, taso, kokonaiseksi saadut rivit.

### Tulokset
Pelin päätyttyä näytetään tulokset, jossa on pelistä saatu pistemäärä, kokonaiseksi saadut rivit ja vaikeustaso.
Lisäksi näytetään painike "Palaa", joka palaa pelivalikkoon.