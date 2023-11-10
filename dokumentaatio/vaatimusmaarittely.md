# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on Tetris peli, jossa tarkoituksena on kerätä pisteitä pudottamalla palikoita ja koota niistä vaakasuoria rivejä. Kun pelaaja saa rivin valmiiksi, se poistuu ja sitä ylempänä olevat palikat putoavat yhden rivin alemmaksi. Lisäksi pelaajan pisteet nousevat. Peli nopeutuu hiljalleen pelin edetessä tasosta riippuen.

## Käyttäjät
Peli on yksin pelattava peli, mutta sovelluksella voi luoda oman profiilin jokaiselle pelaajalle, jolloin jokainen pelaaja pystyy tallentamaan omat pisteensä.

## Suunnitellut toiminnallisuudet

#### Profiilin valitsemis näyttö
Käyttäjä voi luoda uuden profiilin tai pelata vierailijana, jolloin uutta profiilia ei luoda. Profiilin luontiin tarvitaan vain käyttäjänimi, joka täytyy olla uniikki, vähintään 3 merkkiä ja korkeintaan 16 merkkiä pitkä. Käyttäjä voi valita profiilin listasta, jolla haluaa pelata peliä.

#### Aloita peli näyttö
Näytöllä näytetään kolme painiketta: "Aloita peli", "Muuta vaikeustasoa", "Vaihda profiilia". Ensimmäinen painike aloittaa uuden pelin valitulle profiilille. Toinen painike muuttaa pelin vaikeustasoa. Kolmas painike palaa takaisin aloitus näytölle.

#### Peli näyttö
Vasemmassa yläkulmassa näytetään tällä hetkellä putoava palikka. Oikeassa yläkulmassa näytetään 3 seuraavaa palikkaa. Vasemmassa alakulmassa näytetään tilastot: pistemäärä, taso, kokonaiseksi saadut rivit.
Oikeassa alakulmassa on "pause" painike, joka pysäyttää pelin ja näyttää valikon, jossa on seuraavat painikkeet: "Jatka peliä", "Lopeta".

#### Pelin tulokset näyttö
Tässä näytetään pelissä saatu pistemäärä sekä "Pelaa uudelleen" ja "Palaa" painike. Ensimmäinen painike aloittaa uuden pelin. Toinen painike palaa "Aloita peli" näyttöön.

