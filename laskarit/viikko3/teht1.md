```mermaid
classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli

    Ruutu "1" -- "1" Ruututyyppi

    Aloitusruutu "1" --> "1" Ruututyyppi
    Vankila "1" --> "1" Ruututyyppi
    Sattuma_ja_yhteismaa "*" --> "1" Ruututyyppi
    Asemat_ja_laitokset "*" --> "1" Ruututyyppi
    Normaalit_kadut "*" --> "1" Ruututyyppi

    Aloitusruutu "1" -- "1" Monopolipeli
    Vankila "1" -- "1" Monopolipeli

    Ruutu "1" -- "1" Toiminto

    Sattuma_ja_yhteismaa "*" -- "*" Kortti
    Kortti "*" -- "1" Toiminto

    Normaalit_kadut "1" -- "0..4" Talo
    Normaalit_kadut "1" -- "0..1" Hotelli
```