# Ohjelmistotekniikka, harjoitustyö

Sovellus on Tetris peli, jossa tarkoituksena on kerätä pisteitä pudottamalla palikoita ja koota niistä vaakasuoria rivejä. Kun pelaaja saa rivin valmiiksi, se poistuu ja sitä ylempänä olevat palikat putoavat yhden rivin alemmaksi. Lisäksi pelaajan pisteet nousevat. Peli nopeutuu hiljalleen pelin edetessä tasosta riippuen.

## Dokumentaatio
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)

[Release 1](releases/tag/vikko5)

## Asennus
Riippuvuusten asentaminen
```bash
poetry install
```

Sovelluksen käynnistäminen
```bash
poetry run invoke start
```

## Testaus
Testien suorittaminen
```bash
poetry run invoke test
```

Testikattavuusraportin generointi
```bash
poetry run invoke coverage-report
```

## Pylint
Tiedoston [ .pylintrc](.pylintrc) määrittelemien tarkastusten suorittaminen
```bash
poetry run invoke lint
```
