# Käyttöohje


### Ohjelman alustaminen

Asenna riippuvuudet
```
$ poetry install
```

### Ohjelman ajaminen
```
$ poetry run invoke start
```

### Testien ajaminen
```
$ poetry run invoke test
```

### Kattavuusraportin luominen
```
$ poetry run invoke report
```

### Pylintin ajaminen
```
$ poetry run invoke lint
```

## Ohjelman käyttäminen

Ohjelma hyväksyy avainten generointiin luvun väliltä 500-5000.

Salattavaksi tekstiksi max. 127 merkkiä pitkän merkkijonon (hyväksyy kirjaimet, numerot ja erikoismerkit).

Purettavaksi 'koodiksi' samoilla avaimilla salatun tekstin (tämä tulee kenttään automaattisesti).
