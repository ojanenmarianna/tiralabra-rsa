# Vaatimusmäärittely

- Sovellus toteutetaan käyttäen Pythonia. 
- Vertaisarvionnin voin tehdä myös Javalla toteutetuille projekteille. 
- Opinto-ohjelma: TKT
- Projektin dokumentaatio sekä kommentit ovat suomeksi ja koodi englanniksi.

## Projekti

Toteutan tietorakenteet ja algoritmit -harjoitustyönä RSA-salaus generaattorin. Kyseessä on yksisuuntainen modulaari funktio, joka on helppo laskea mutta todella hankalaa ja aikaa vievää laskea taaksepäin.

RSA perustuu kahteen matemaattiseen ongelmaan: 

- RSA ongelmaan, ja
- suurten lukujen tuottamisen ongelmaan

Molemmat ongelmat on mielletty NP-täydellisiksi eli mikään olemassa oleva algoritmi ei pysty ratkaisemaan niitä tehokkaasti.
RSA-algoritmi sisältää neljä eri vaihetta; avaimen luonti, avaimen jako, salaus ja salauksen purkaminen.
Avainten luonnissa tarvitaan mahdollisimman isoja satunnaisesti valittuja alkulukuja eli tarvitaan nopea ja luotettava alkulukutesti.

### Tarvittavat algoritmit:

- Laajennettu Eukleiden algoritmi. Aikavaativuus: O({logn}2)
- Potenssiinkorotusalgoritmi
- Alkulukutesti esim. Miller-Rabin. Aikavaativuus: O(k log3n)
- Aikavaativuus yhteensä: O({logn}3)



### Lähteet

- [RSA-salausalgortimit ja alkuluvut](https://trepo.tuni.fi/bitstream/handle/10024/78940/gradu02474.pdf?sequence=1&isAllowed=y)
- [Wikipedia: RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [Wikipedia: Miller-Rabin test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
- [Wkipedia: Carmichael function](https://en.wikipedia.org/wiki/Carmichael_function)
- [Wikipedia: Primality test](https://en.wikipedia.org/wiki/Primality_test)
- [e.e.a.com](https://www.extendedeuclideanalgorithm.com/xea.php)
- Chandel, Sonali & Cao, Wenxuan & Sun, Zijing & Yang, Jiayi & Zhang, Bailu & Ni, Tian-Yi. (2020). A Multi-dimensional Adversary Analysis of RSA and ECC in Blockchain Encryption. 10.1007/978-3-030-12385-7_67. 
