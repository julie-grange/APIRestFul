# API Base Carbone
Ceci est une API RestFul développé dans le cadre d'un test technique. 

L'API utilise une base de donnée "base-carbone.csv" issue d'un extrait de la base disponible sur le site de l'ADEME https://data.ademe.fr/datasets/base-carbone(r). 

Cette API tourne dans un container. 

Le code de l'API est dans le fichier /main.py

## Composition de la base de données

* Id : identifiant de la ligne
* Name : Nom de l'objet en français
* Unit : unité de l'émission
* CO2f : quantité de CO2f
* CH4f : quantité CH4f
* CH4b : quantité de CH4b
* N2O : quantité de NO2
* CO2b : quantité de CO2b

## Installation
### 1-builder image : 
`$ docker build --tag api-base-carbone .`

### 2-Lancer image :
`$ docker run -p 5000:5000 api-base-carbone`

## API REST
Voici la liste des requêtes pouvant être exécutées

### GET Base de données
Récupération de la base de données
#### Requête

```
curl --location --request GET 'http://localhost:5000/base/'
```

#### Réponse 
```
Status: 200 OK
Content-Type: application/json
Content-Length: 6097

{
  "data": {
    "CH4b": {
      "0": "0", 
      "1": "0", 
      "2": "0", 
      "3": "0", 
      "4": "0,0726", 
      "5": "1,16E-03", 
      "6": "0", 
      "7": "0", 
      "8": "0", 
      "9": "0", 
      "10": "0", 
      "11": "0", 
      "12": "0", 
      "13": "0", 
      "14": "0", 
      "15": "0", 
      "16": "0", 
      "17": "0", 
      "18": "0", 
      "19": "0", 
      "20": "0", 
      "21": "0", 
      "22": "0", 
      "23": "0", 
      "24": "0,0511", 
      "25": "0", 
      "26": "0", 
      "27": "0", 
      "28": "0", 
      "29": "0", 
      "30": "0,0482", 
      "31": "0"
    }, ...
```

### GET liste objets
Obtention de la liste des objets
#### Requête

```
curl --location --request GET 'http://localhost:5000/base/objects'
```

#### Réponse 

```
Status: 200 OK
Content-Type: application/json
Content-Length: 972

{
  "Object": {
    "0": "Bateau automoteur", 
    "1": "Bateau automoteur", 
    "2": "Bateau automoteur", 
    "3": "Bateau pousseur", 
    "4": "Bois b\u00fbche", 
    "5": "Broyats de cagettes et de pallettes", 
    "6": "Carton", 
    "7": "Carton", 
    "8": "Carton", 
    "9": "Circuits imprim\u00e9s", 
    "10": "Circuits imprim\u00e9s", 
    "11": "D\u00e9chets alimentaires", 
    "12": "Ecorces, sciures, broyats \u2026", 
    "13": "Ecran \u00e0 cristaux liquides", 
    "14": "Essence", 
    "15": "Essence", 
    "16": "Essence", 
    "17": "Essence", 
    "18": "Essence", 
    "19": "Essence", 
    "20": "Gazole", 
    "21": "Gazole non routier", 
    "22": "Gazole routier", 
    "23": "Gazole routier", 
    "24": "Granul\u00e9s bois", 
    "25": "Ordures m\u00e9nag\u00e8res", 
    "26": "Paille", 
    "27": "Paille", 
    "28": "Papier", 
    "29": "Papier", 
    "30": "Plaquettes foresti\u00e8res", 
    "31": "plaquettes foresti\u00e8res"
  }
}

```

### GET Objet particulier
Obtenir les informations liés à un objet en particulier. 
Utiliser le nom de l'objet "Name".
#### Requête 
```
curl --location --request GET 'http://localhost:5000/base/objects/Id?Name=Papier'
```

#### Réponse 
```
Status: 200 OK
Content-Type: application/json
Content-Length: 517

{
    "Id": {
        "CH4b": {
            "28": "0",
            "29": "0"
        },
        "CH4f": {
            "28": "0",
            "29": "0"
        },
        "CO2b": {
            "28": "1393",
            "29": "1393,333333"
        },
        "CO2f": {
            "28": "36",
            "29": "0"
        },
        "Id": {
            "28": 14222,
            "29": 14242
        },
        "N2O": {
            "28": "2809",
            "29": "2809"
        },
        "Name": {
            "28": "Papier",
            "29": "Papier"
        },
        "Unit": {
            "28": "kgCO2e/tonne",
            "29": "kgCO2e/tonne"
        }
    }
}
```

### POST Nouvel Object
Ajouter un nouveau objet dans la base de donnée. 
Fournir obligatoirement le nom de l'objet ("Name") et la quantité de CO2 associée ("CO2b"). 
#### Requête 

```
curl --location --request POST 'http://localhost:5000/base/objects/Id?Name=X&CO2b=12'
```

#### Réponse 
```
Status: 200 OK
Content-Type: application/json
Content-Length: 6318

{
    "Base mise à jour": {
        "CH4b": {
            "0": "0",
            "1": "0",
            "2": "0",
            "3": "0",
            "4": "0,0726",
            "5": "1,16E-03",
            "6": "0",
            "7": "0",
            "8": "0",
            "9": "0",
            "10": "0",
            "11": "0",
            "12": "0",
            "13": "0",
            "14": "0",
            "15": "0",
            "16": "0",
            "17": "0",
            "18": "0",
            "19": "0",
            "20": "0",
            "21": "0",
            "22": "0",
            "23": "0",
            "24": "0,0511",
            "25": "0",
            "26": "0",
            "27": "0",
            "28": "0",
            "29": "0",
            "30": "0,0482",
            "31": "0",
            "32": NaN
        },
        "CH4f": {
            "0": "0,0137",
            "1": "8,22E-03",
            "2": "9,40E-03",
            "3": "0,0106",
            "4": "0",
            "5": "0",
            "6": "0",
            "7": "0",
            "8": "137",
            "9": "21,1",
            "10": "27,1",
            "11": "0",
            "12": "0",
            "13": "5,6",
            "14": "23,4",
            "15": "2,97E-03",
            "16": "2,91E-03",
            "17": "3,93",
            "18": "23,3",
            "19": "23,7",
            "20": "0,0214",
            "21": "1,21",
            "22": "1,32",
            "23": "1,17",
            "24": "0",
            "25": "12240",
            "26": "0",
            "27": "0",
            "28": "0",
            "29": "0",
            "30": "0",
            "31": "0",
            "32": NaN
        },
        "CO2b": {
            "0": "1,764467014",
            "1": "1,060165223",
            "2": "1,212188378",
            "3": "1,36234151",
            "4": "1,466666667",
            "5": "1,466666667",
            "6": "1393",
            "7": "1393,333333",
            "8": "169,9189333",
            "9": "10,2128575",
            "10": "13,192775",
            "11": "146,3",
            "12": "1280",
            "13": "1,3793125",
            "14": "198,478391",
            "15": "1,29088791",
            "16": "1,290888",
            "17": "1728,096259",
            "18": "156,140338",
            "19": "154,001368",
            "20": "19,953016",
            "21": "112,5939674",
            "22": "184,495797",
            "23": "191,8484",
            "24": "1,686666667",
            "25": "142,6552336",
            "26": "1,39",
            "27": "1390",
            "28": "1393",
            "29": "1393,333333",
            "30": "1,375",
            "31": "1110",
            "32": "12"
        },
        "CO2f": {
            "0": "30,3",
            "1": "18,2",
            "2": "20,8",
            "3": "23,4",
            "4": "0",
            "5": "0",
            "6": "36",
            "7": "0",
            "8": "33,3",
            "9": "312",
            "10": "398",
            "11": "0",
            "12": "0",
            "13": "46,9",
            "14": "2860",
            "15": "0,364",
            "16": "0,36",
            "17": "482",
            "18": "2860",
            "19": "2860",
            "20": "53,6",
            "21": "3029",
            "22": "3309",
            "23": "2943",
            "24": "0",
            "25": "0",
            "26": "0",
            "27": "0",
            "28": "36",
            "29": "0",
            "30": "0",
            "31": "0",
            "32": NaN
        },
        "Id": {
            "0": 21478.0,
            "1": 21480.0,
            "2": 21479.0,
            "3": 21476.0,
            "4": 14219.0,
            "5": 14231.0,
            "6": 22030.0,
            "7": 22032.0,
            "8": 24237.0,
            "9": 24236.0,
            "10": 22037.0,
            "11": 14235.0,
            "12": 24243.0,
            "13": 14005.0,
            "14": 13989.0,
            "15": 25766.0,
            "16": 25769.0,
            "17": 25760.0,
            "18": 25762.0,
            "19": 25770.0,
            "20": 13992.0,
            "21": 25777.0,
            "22": 25779.0,
            "23": 14225.0,
            "24": 22063.0,
            "25": 14238.0,
            "26": 14239.0,
            "27": 22022.0,
            "28": 14222.0,
            "29": 14242.0,
            "30": 22030.0,
            "31": 22022.0,
            "32": NaN
        },
        "N2O": {
            "0": "0,244",
            "1": "0,146",
            "2": "0,167",
            "3": "0,188",
            "4": "0",
            "5": "0",
            "6": "2809",
            "7": "2809",
            "8": "-988450",
            "9": "4",
            "10": "6,09",
            "11": "0",
            "12": "0",
            "13": "0,226",
            "14": "23,5",
            "15": "2,99E-03",
            "16": "2,92E-03",
            "17": "3,94",
            "18": "23,8",
            "19": "23,8",
            "20": "0,435",
            "21": "24,6",
            "22": "26,9",
            "23": "23,9",
            "24": "0",
            "25": "0",
            "26": "0",
            "27": "0",
            "28": "2809",
            "29": "2809",
            "30": "0",
            "31": "0",
            "32": NaN
        },
        "Name": {
            "0": "Bateau automoteur",
            "1": "Bateau automoteur",
            "2": "Bateau automoteur",
            "3": "Bateau pousseur",
            "4": "Bois bûche",
            "5": "Broyats de cagettes et de pallettes",
            "6": "Carton",
            "7": "Carton",
            "8": "Carton",
            "9": "Circuits imprimés",
            "10": "Circuits imprimés",
            "11": "Déchets alimentaires",
            "12": "Ecorces, sciures, broyats …",
            "13": "Ecran à cristaux liquides",
            "14": "Essence",
            "15": "Essence",
            "16": "Essence",
            "17": "Essence",
            "18": "Essence",
            "19": "Essence",
            "20": "Gazole",
            "21": "Gazole non routier",
            "22": "Gazole routier",
            "23": "Gazole routier",
            "24": "Granulés bois",
            "25": "Ordures ménagères",
            "26": "Paille",
            "27": "Paille",
            "28": "Papier",
            "29": "Papier",
            "30": "Plaquettes forestières",
            "31": "plaquettes forestières",
            "32": "X"
        },
        "Unit": {
            "0": "kgCO2e/véhicule.km",
            "1": "kgCO2e/véhicule.km",
            "2": "kgCO2e/véhicule.km",
            "3": "kgCO2e/véhicule.km",
            "4": "kgCO2e/kg",
            "5": "kgCO2e/kg",
            "6": "kgCO2e/tonne",
            "7": "kgCO2e/tonne",
            "8": "kgCO2e/tonne",
            "9": "kgCO2e/m²",
            "10": "kgCO2e/m²",
            "11": "kgCO2e/tonne",
            "12": "kgCO2e/tonne",
            "13": "kgCO2e/unité",
            "14": "kgCO2e/tep PCI",
            "15": "kgCO2e/litre",
            "16": "kgCO2e/litre",
            "17": "kgCO2e/tonne",
            "18": "kgCO2e/tep PCI",
            "19": "kgCO2e/tonne",
            "20": "kgCO2e/GJ PCI",
            "21": "kgCO2e/tep PCI",
            "22": "kgCO2e/tonne",
            "23": "kgCO2e/tep PCI",
            "24": "kgCO2e/kg",
            "25": "kgCO2e/tonne",
            "26": "kgCO2e/kg",
            "27": "kgCO2e/tonne",
            "28": "kgCO2e/tonne",
            "29": "kgCO2e/tonne",
            "30": "kgCO2e/kg",
            "31": "kgCO2e/tonne",
            "32": NaN
        }
    }
}
```


