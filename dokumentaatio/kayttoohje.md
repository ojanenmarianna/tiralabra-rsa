# Käyttöohje

Miten ohjelma suoritetaan, miten eri toiminnallisuuksia käytetään
Minkä muotoisia syötteitä ohjelma hyväksyy
Missä hakemistossa on jar ja ajamiseen tarvittavat testitiedostot.

#### Ohjelman alustaminen

Asenna riippuvuudet
```
$ poetry install
```

#### Ohjelman ajaminen
```
$ poetry run invoke start
```

#### Testien ajaminen
```
$ poetry run invoke test
```

#### Kattavuusraportin luominen
```
$ poetry run invoke coverage_report
```

#### Pylintin ajaminen
```
$ poetry run invoke lint
```
