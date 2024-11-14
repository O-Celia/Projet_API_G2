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

## Stratégie de tests

1. Niveaux de tests

- **Tests unitaires** : Tests des composants individuels de l'application, tels que les fonctions et méthodes (test de la route *home*, et des requêtes *get*, *create*, *update*, *delete*). 
- **Tests fonctionnels** : Vérification que les fonctionnalités de l'application répondent aux attentes définies, en se basant sur des critères spécifiques (tests des requêtes *get, *create*, *update*, *delete*).
- **Tests d'intégration** : Tests visant à s'assurer que les différents modules et composants de l'application fonctionnent correctement ensemble (tests des requêtes *get, *create*, *update*, *delete*).
- **Tests de performance** : Évaluations de la réactivité et de la charge de l'application pour garantir que l'API peut supporter une utilisation à grande échelle (tests de charge et de temps de réponse).

2. Objectifs des tests

Les objectifs principaux de cette stratégie de tests sont :
- Vérifier la bonne fonctionnalité de l'application selon les exigences.
- S'assurer de la stabilité et de la performance de l'API sous diverses charges.
- Identifier et corriger les anomalies avant la livraison finale.

3. Responsabilités

Les responsabilités concernant les tests sont réparties comme suit :
- **Développeur** : Écriture des tests unitaires et d'intégration pour les différents endpoints de l'API. Validation de la fonctionnalité des routes GET, POST, PATCH, DELETE.
- **Testeur/QA** : Exécution des tests de performance (test de charge et test de temps de réponse). Validation des cas d'erreur (404, 500) et de l'interface utilisateur.
- **Chef de projet** : Suivi de l'avancement des tests, gestion des risques et validation des tests finaux.

4. Tâches principales

Les tâches principales associées aux tests sont :
- Mise en place des tests unitaires fonctionnels d'intégration pour valider les comportements attendus de fonctionnalité clé de l'application et pour vérifier la communication entre les différents modules et composants.
- Tests de performance pour évaluer le temps de réponse et la capacité de charge de l'application.
- Vérification des cas d'erreur pour s'assurer que l'API répond correctement aux situations exceptionnelles.

5. Critères d'entrée et de sortie

### Critères d'entrée
- Code fonctionnel prêt à être testé.
- Accès à l'environnement de test.
- Données de test préparées pour les tests fonctionnels et de performance.
- Accès aux outils de test nécessaires (frameworks de test comme `unittest`, outils de performance).

### Critères de sortie
- Tous les tests passent avec succès (tests fonctionnels et non-fonctionnels).
- Les rapports de tests sont générés, détaillant les résultats et les éventuels bugs ou problèmes.
- Les performances de l'application sont dans les limites acceptables.
- Les tests ont couvert les cas de bord, les erreurs possibles, et la charge attendue.

6. Risques

Les risques potentiels associés aux tests incluent :
- **Risque de non-complétude** : Tous les scénarios de test ne sont peut-être pas couverts.
- **Problèmes de performance non identifiés** : Le test de charge peut ne pas avoir été réalisé sous des conditions suffisamment extrêmes.
- **Bugs de dernière minute** : De nouveaux bugs peuvent apparaître au moment de l'intégration des dernières fonctionnalités.

## Utilisation

Pour utiliser l'application mise en place:
```code
uvicorn src.main:app --reload
```

Accéder à la page : localhost:8000  <br/>
Affichage swagger : localhost:8000/docs

## Tests

Tests pour la route Client:
```code
python -m test.client
```

Tests pour la route Commande:
```code
python -m test.commande
```

Tests pour la route Detail des commandes:
```code
python -m test.detail_commande
```

Tests pour la route Objet:
```code
python -m test.objet
```