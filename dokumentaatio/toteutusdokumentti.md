# Toteutusdokumentti

## Ohjelman yleisrakenne

### Luokat

#### RsaService

Luokka on vastuussa Rsa-avaimen luonnista

1. Generoidaan satunnaiset alkuluvut p ja q niin, että p on erisuuuri kuin q, luvut ovat n-bittiä pitkiä
2. Tehdään alkuluvuille ensin yksinkertainen alkulukutesti (trial_division) ja jos luvut pääsevät tästä läpi niin
3. Tehdään alkuluvuille Miller-Rabin alkuluku -testi 40 kertaa (40 on tässä testissä optimaalinen määrä). 
4. Lasketaan alkuluvuista modulus = p*q
5. Lasketaan lambda Carmichaelin funktiolla
6. Lasketaan yksityisen avaimen eksponentti d moduluksella ja julkisen avaimen eksponentilla (Python 3.8 eteenpäin voidaan laskea suoraan funktiolla pow())
7. Luodaan julkinen avain moduluksella ja julkisen avaimen eksponentilla e
8. Luodaan yksityinen avain moduluksella ja yksityisen avaimeneksponentilla d.

#### RsaKey

Luokka on vastuussa rsa-avain -olion luomisesta.

1. Luo avaimen annetulla moduluksella ja eksponentilla
2. Palauttaa avaimen moduluksen ja eksponentin gettereillä

#### EncryptionDecryptionService

Luokka on vastuussa viestin salaamisesta ja salatun viestin purkamisesta.

1. Salaa viestin muuttamalla tekstin ensin tavuiksi ja sitten kokonaisluvuksi.
2. Purkaa viestin muuttamalla ensin kokonaisluvun tavuiksi ja sitten tavut tekstiksi.


#### PrimeService

Luokka on vastuussa alkulukulistan luomisesta rsa-avaimen alkulukuehdokkaiden alkulukutestejä varten.

1. Luo listan annettuun lukuun asti (1500), jossa on pelkästään alkulukuja.

## Saavutetut aika- ja tilavaativuudet

- Trial division alkulukutestin saavutettu aikavaativuus on O(sqrt(N)).


## Työn mahdolliset puutteet ja parannusehdotukset

- Ohjelma toimii vain alle 128 merkkiä pitkillä syötteillä. Yksi parannusehdotus olisikin siis toteuttaa toiminnallisuus niin, että syötteet voisivat olla pidempiä.
- Pitkiä syötteitä varten voitaisiin toteuttaa viestin 'pehmustaminen' (padding), eli viestiin lisättäisiin randomia dataa, joka auttaa estämään useita hyökkäyksiä piilottamalla viestin todellisen rakenteen.
- Ohjelma ei tallenna avaimia mihinkään, parannuksena voitaisiin toteuttaa julkisen ja yksityisen avaimen tallennus esim. johonkin ennalta määriteltyyn tiedostoon.
- Tärkeille luvuille, kuten yksityisen avaimen eksponentti d sekä alkuluvuille p ja q tulisi toteuttaa tarkemmat ehdot, sillä pelkkä eriarvoisuus ei takaa turvallisuutta.
  - Jos p ja q ovat liian lähellä toisiaan, ne on helppo löytää
  - Jos yksityisen avaimen eksponentti d on liian pieni, se on helppo selvittää 


## Lähteet

- [Modular multiplicative inverse in Python](https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python)
- [What is RSA encryption and how does it work?](https://www.comparitech.com/blog/information-security/rsa-encryption/)
- [RSA-salausalgortimit ja alkuluvut](https://trepo.tuni.fi/bitstream/handle/10024/78940/gradu02474.pdf?sequence=1&isAllowed=y)
- [RSA Algorithm in Cryptography](https://www.geeksforgeeks.org/rsa-algorithm-cryptography/)
- [e.e.a.com](https://www.extendedeuclideanalgorithm.com/xea.php)
- [Prime Curious](https://primes.utm.edu/curios/index.php?start=37&stop=96)
- [Wikipedia: RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [Wikipedia: Miller-Rabin test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
- [Wkipedia: Carmichael function](https://en.wikipedia.org/wiki/Carmichael_function)
- [Wikipedia: Primality test](https://en.wikipedia.org/wiki/Primality_test)
- Chandel, Sonali & Cao, Wenxuan & Sun, Zijing & Yang, Jiayi & Zhang, Bailu & Ni, Tian-Yi. (2020). A Multi-dimensional Adversary Analysis of RSA and ECC in Blockchain Encryption. 10.1007/978-3-030-12385-7_67. 
