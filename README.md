# Système de surveillance des prix ... 

## <span style="color:#F79F07">Description</span>

---


## <span style="color:#F79F07">Installation du projet</span>
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

<br>



## <span style="color:#F79F07">Exécution du projet</span>
Le projet se compose d'un package `scraping` qui contient les différentes fonctionnalités et d'un fichier `main.py` qui est le point d'entrée de l'application. 
Pour exécuter le projet, la commande est la suivante : 
``` 
python main.py
```

> Cette commande doit être exécutée à partir du dossier du projet

---
  
  


## <span style="color:#F79F07">Données produites</span>

Un dossier `data` composé de deux sous-dossiers se créent pendant l'exécution du code :

- `Csv` : les fichiers csv de chaque catégorie avec des informations sur tous les livres d'une  même catégorie 
- `Img` : les images de chaque livre identifiées par une catégorie et un titre de livre.



---


