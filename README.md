# Projet_Devops - ZoukMachine

La **ZoukMachine** permet de générer une playlist basée sur un de vos titres favoris. Si la musique recherchée n'est pas disponible dans notre base de données, l'application interagit avec l'API Spotify pour récupérer les informations correspondantes. L'interface utilisateur offre également la possibilité d'ouvrir le titre directement dans Spotify.

## Prérequis

Pour utiliser notre application vous aurez besoin de **docker** ainsi que **MongoDB**.

## Installation

Tout d'abord, clonez le repository avec la commande suivante dans le répertoire de votre choix:\
 `git clone https://github.com/Jacqkues/Projet_Devops.git`

Ensuite, il vous faudra initialiser la base de donnée Mongo. Pour ce faire, créez une connexion avec comme URI:\
`mongodb://admin:admin@localhost/admin`.\
La connexion établie, créez une database `devOpsBDD` ainsi qu'une collection `SpotifySongs`.\
Maintenant, glissez le fichier csv que vous trouverez ici: `Projet_Devops/backend/data/spotify_data.csv`

Enfin, si vous lancez l'application pour la première fois sur votre machine, exécutez la commande suivante:\
`docker compose up --build`.

Pour les prochaines fois, un simple `docker compose up` suffira.

Vous pouvez maintenant aller sur votre localhost pour profiter de la ZoukMachine.

## Utilisation
