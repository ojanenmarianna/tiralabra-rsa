# Testausdokumentti

## Yksikkötestauksen kattavuusraportti

![plot](https://github.com/ojanenmarianna/tiralabra-rsa/blob/main/dokumentaatio/kuvat/kattavuusraportti.jpg)

## Mitä on testattu, miten tämä tehtiin

Projektissa testataan yksikkötesteillä RSA-avainten luonnin ja viestien salaamisen sekä purkamisen kannalta tärkeimpiä ominaisuuksia.

Testejä varten luodaan kaksi suurta (512 bittistä) alkulukua, yhdistetty luku sekä testi-RsaService.
ALkuluvut p ja q on etsitty kirjallisuudesta, jotta voidaan olla varmoja, että ne todella ovat alkulukuja.

## TestRsaService -luokka

Testaa RsaServicen metodien toimintaa, mm. compute_lambdan, trial_division...

### Tärkeimmät testit:

1. Rabin-Miller -testi testaa, että metodi palauttaa vain alkuluvuille True arvon, yhdistetyille luvuille aina False.
2. Encryption ja decryption -testi testaa, että viestin salaaminen ja salatun viestin purkaminen toimii aina oikein.


