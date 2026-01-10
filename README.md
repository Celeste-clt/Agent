# Agent Python – Musique / Fichiers / Événements / Mails

[Lien git ](https://github.com/Celeste-clt/Agent)

## Description

**Agent** est un assistant terminal en Python qui permet de :

- Jouer des musiques depuis un dossier local
- Créer, modifier et supprimer des fichiers texte
- Ajouter des événements dans un calendrier
- Simuler l’envoi de mails en enregistrant les informations dans un fichier JSON

L’utilisateur interagit avec l’agent en **langage avec des phrases ou des mots-clés**.

# Installation et structure

1. Cloner le dépôt :

```
git clone https://github.com/Celeste-clt/Agent.git

cd Agent

Agent/
├─ main.py
├─ music.py
├─ add.py
├─ agenda.py
├─ mail.py
├─ mails.json
├─ events.txt
└─ musique/
```

# Lancement

python3 main.py

# Musique

**Mots clés**

```
> musique - joue
> Quel fichier audio ? Travis-Scott.mp3
> Lancement de musique/Travis-Scott.mp3...
```

_Important_ titre de la musique : Travis-Scott

# Fichier

## creation

**Mots clés**

```
> crée un fichier - creer - fichier
> Nom du fichier : test.txt
> Écris le contenu du fichier :
> Bonjour tout le monde
> Fichier 'test.txt' créé.
```

_Important_ mettre le .txt

## Modification

```
> modifie le fichier - modifie
> Nom du fichier : test.txt
> Nouveau contenu :
> Bonjour tout le monde ! Modifié.
> Fichier 'test.txt' modifié.
```

## Supprimer

```
> supprime le fichier - supprime
> Nom du fichier : test.txt
> Fichier 'test.txt' supprimé.
```

_Important_ écrire le fichier en entier avec le txt

# Ajouter un évènement

```
> événement - (ou phrase complete) : crée moi un événement le 12/03/2026 à Annecy titre Anniversaire

> Date de l'événement (JJ/MM/AAAA) : 12/03/2026
> Lieu : Annecy
> Titre : Anniversaire
> Événement ajouté
```

_Important_ mettre la date en entier comme ceci : (JJ/MM/AAAA)

# Mail

Mail ajouté dans mails.json

```
> envoie un mail
> Destinataire : test@gmail.com
> Sujet : Bonjour
> Contenu : xxxx
> Mail enregistré
```

# Stoper la conversation

```
> quit
> À bientôt !
```
