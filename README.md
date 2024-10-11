# Projet DevOps - ZoukMachine

La **ZoukMachine** permet de générer une playlist basée sur un de vos titres favoris. Si la musique recherchée n'est pas disponible dans notre base de données, l'application interagit avec l'API Spotify pour récupérer les informations correspondantes.\
L'interface utilisateur offre également la possibilité d'ouvrir le titre directement dans Spotify.

## Prérequis

Pour utiliser notre application, vous aurez besoin de :

- **Docker**

## Installation

Suivez ces étapes pour installer l'application :

1. **Cloner le repository :**

   Exécutez la commande suivante dans le répertoire de votre choix :

   ```bash
   git clone https://github.com/Jacqkues/Projet_Devops.git
   ```

2. **Charger les données :**

   Glissez le fichier CSV dans la collection devOpsBDD que vous trouverez ici :

   ```bash
   Projet_Devops/backend/data/spotify_data.csv
   ```

3. **Lancer l'application :**

   Si vous lancez l'application pour la première fois sur votre machine, exécutez la commande suivante :

   ```bash
   docker compose up --build
   ```

   Pour les prochaines fois, vous pourrez simplement exécuter la commande sans l'option `build`.

4. **Accéder à l'application :**

   Ouvrez votre navigateur et allez sur [`http://localhost`](http://localhost) pour profiter de la ZoukMachine.

## Utilisation

Pour utiliser la **ZoukMachine**, suivez les étapes ci-dessous :

1. **Lancer l'application :**

   - Ouvrez votre navigateur web et allez à l'adresse suivante : [`http://localhost`](http://localhost).

2. **Rechercher une chanson :**

   - Dans le champ de recherche, entrez le titre de votre chanson favorite que vous souhaitez ajouter à votre playlist.
   - Appuyez sur `Entrée`.

3. **Vérification de la disponibilité :**

   - L'application vérifiera si le titre est disponible dans notre base de données.
   - Si la chanson n'est pas disponible, l'application interagira avec l'API Spotify pour récupérer des informations sur des chansons similaires ou associées.

4. **Génération de la playlist :**

   - Une fois la recherche terminée, la playlist sera générée et affichée à l'écran suivant les caractéristiques de la chanson en entrée.

5. **Écouter la musique :**
   - Vous pouvez cliquer sur chaque titre de la playlist pour l'écouter directement sur Spotify.
   - Si vous avez l'application Spotify installée, le titre s'ouvrira directement dans celle-ci.
