# Tiralabra Rsa-generaattori
![GitHub Actions](https://github.com/ojanenmarianna/tiralabra-rsa/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/ojanenmarianna/tiralabra-rsa/branch/main/graph/badge.svg?token=T2aLuiwMUD)](https://codecov.io/gh/ojanenmarianna/tiralabra-rsa) 

Tässä repositoriossa on toteutettu Helsingin yliopiston Tietorakenteet ja algoritmit laboratoriotyö.

## Dokumentaatio

[Käyttöohje](./dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

[Toteutusdokumentti](./dokumentaatio/toteutusdokumentti.md)

[Testausdokumentti](./dokumentaatio/testausdokumentti.md)


## Ohjelman alustaminen

Asenna riippuvuudet
```
$ poetry install
```

## Ohjelman ajaminen
```
$ poetry run invoke start
```

## Testien ajaminen
```
$ poetry run invoke test
```

## Kattavuusraportin luominen
```
$ poetry run invoke report
```

## Pylintin ajaminen
```
$ poetry run invoke lint
```
