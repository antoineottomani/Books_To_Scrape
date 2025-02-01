# Système de surveillance des prix d'un libraire

## Description
Ce programme réalisé en Python permet d'extraire automatiquement les informations tarifaires du site [Books To Scrape](http://books.toscrape.com/) ainsi que les couvertures de chaque livre.

---

## Installation du projet
1. Le code source est disponible depuis Github :
```
git clone https://github.com/antoineottomani/OCR_Project02.git
```

2. Créer l'environnement virtuel puis l'activer:
```
python3 -m venv env
source env/bin/activate
```

3. Des paquets spécifiques sont nécessaires pour le fonctionnement du code, ils sont listés dans le fichier `requirements.txt`. Il suffit ensuite de les installer dans l'environnement virtuel :
```
pip install -r requirements.txt
```

---

## Exécution du projet 
  

Le projet se compose d'un package `scraping` qui contient les différentes fonctionnalités et d'un fichier `main.py` qui est le point d'entrée de l'application. 
Pour exécuter le projet, la commande est la suivante : 
``` 
python main.py
```

> Cette commande doit être exécutée à partir du dossier du projet

---

## Données produites

Un dossier `data` composé de deux sous-dossiers sont créés pendant l'exécution du code :

- `Csv` : les fichiers csv de chaque catégorie avec des informations sur tous les livres d'une  même catégorie 
- `Img` : les images de chaque livre identifiées par une catégorie et un titre de livre.


---


