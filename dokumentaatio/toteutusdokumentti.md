# Toteutusdokumentti

## Ohjelman yleisrakenne

### Luokat

#### Rsa_service

Luokka on vastuussa Rsa-avaimen luonnista

1. Generoidaan satunnaiset alkuluvut p ja q niin, että p on erisuuuri kuin q, luvut ovat n-bittiä pitkiä
2. Tehdään alkuluvuille ensin yksinkertainen alkulukutesti (trial_division) ja jos luvut pääsevät tästä läpi niin
3. Tehdään alkuluvuille Miller-Rabin alkuluku -testi 40 kertaa (40 on tässä testissä optimaalinen määrä). 
4. Lasketaan alkuluvuista modulus = p*q
5. Lasketaan lambda Carmichaelin funktiolla
6. Lasketaan yksityisen avaimen eksponentti d moduluksella ja julkisen avaimen eksponentilla (Python 3.8 eteenpäin voidaan laskea suoraan funktiolla pow())
7. Luodaan julkinen avain moduluksella ja julkisen avaimen eksponentilla e
8. Luodaan yksityinen avain moduluksella ja yksityisen avaimeneksponentilla d.

#### Rsa_key

Luokka on vastuussa rsa-avain -olion luomisesta.

1. Luo avaimen annetulla moduluksella ja eksponentilla
2. Palauttaa avaimen moduluksen ja eksponentin gettereillä

#### Encryption_decryption_service

Luokka on vastuussa viestin salaamisesta ja salatun viestin purkamisesta.

1. Salaa viestin muuttamalla tekstin ensin tavuiksi ja sitten kokonaisluvuksi.
2. Purkaa viestin muuttamalla ensin kokonaisluvun tavuiksi ja sitten tavut tekstiksi.


#### Prime_service

Luokka on vastuussa alkulukulistan luomisesta rsa-avaimen alkulukuehdokkaiden alkulukutestejä varten.

1. Luo listan, jossa pelkästään alkulukuja, annettuun lukuun asti (1500).

## Saavutetut aika- ja tilavaativuudet

1. Trial division alkulukutestin saavutettu aikavaativuus on O(sqrt(N)).


## Työn mahdolliset puutteet ja parannusehdotukset


## Lähteet

[Modular multiplicative inverse in Python](https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python)
