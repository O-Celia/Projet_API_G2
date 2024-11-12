# Projet_API_G2

Projet TP7 : Développement d'une application web

Réalisation d'une refonte du backend de l'application de gestion de Digicheese pour l'accès aux clients, commandes et détails des commandes.

## Membres

AICHOUNE Wafa <br/>
GUILLAIN Claire <br/>
OUEDRAOGO Célia <br/>
ZARDI Yakine

## Configuration

1. Créer un environnement virtuel:

Avec Linux/Mac:
```code
env python -m venv .venv
```
Sur certaines distribution Linus/MAcOS, il faut utiliser *python3*

Avec Windows:
```code
python -m venv .venv
```

**Activer venv:**

Avec Linux/Mac:
```code
source .venv/bin/activate
```

Avec Windows: 
```code
.venv\Scripts\activate.ps1
```
Dans le cas où les scripts sont désactivés sur le système pour Windows:
```code
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

**Pour sortir de l'environnement virtuel:**

```code
deactivate
```

2. Installer les packages Python nécessaires

```code
pip install -r requirements.txt
```

3. Créer les variables d'environnement

- Créer un fichier .env
- Créer une variable Utilisateur et renseigner le nom d'utilisateur utilisé pour se connecter au serveur MySQL
- Créer une variable Password et renseigner le mot de passe utilisé pour se connecter au serveur MySQL
- Créer une variable host et renseigner l'hôte utilisé pour se connecter au serveur MySQL (généralement, localhost)
- Créer une variable connector et renseigner le connector utilisé (mysql ou mysql+pymysql)

**Attention: si l'accès au serveur ne nécessite pas de mot de passe (ce qui n'est pas prudent, à éviter), il faut commenter la ligne 20 et décommenter la ligne 21 dans le fichier src/database.py. Si l'accès au serveur nécessite un mot de passe, il faut décommenter la ligne 20 et commenter la ligne 21 dans le fichier src/database.py.**

4. Créer la base de données

Lancer le fichier create_db.sql sur le serveur MySQL

## Utilisation

Pour utiliser l'application mise en place:
```code
uvicorn src.main:app --reload
```