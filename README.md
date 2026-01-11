# Agent Python – Musique / Fichiers / Événements / Mails

[Lien git ](https://github.com/Celeste-clt/Agent)

## Description

**Agent** est un assistant terminal en Python qui permet de :

- Jouer des musiques depuis un dossier local
- Créer, modifier et supprimer des fichiers texte
- Ajouter des événements dans un calendrier
- Simuler l’envoi de mails en enregistrant les informations dans un fichier JSON

Cet agent utilise LLaMA local pour répondre aux attentes de l'utilisateur

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

# Installation

```
pip install -r requirements.txt
```

## Installer llama

```
brew install llama.cpp
```

## Lancer le serveur

```
llama-server -hf bartowski/Llama-3.2-3B-Instruct-GGUF:Q8_0
```

```
Port : http://127.0.0.1:8080
```

# Musique

```
> musique - joue
> Quel fichier audio ? Travis-Scott.mp3
> Lancement de musique/Travis-Scott.mp3...
```

_Important_ titre de la musique : Travis-Scott

# Fichier

## creation

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
Option à chosir :
Que veux-tu faire avec les mails ?
1. Créer un mail
2. Compter les mails
3. Lister les mails
4. Lire un mail
5. Supprimer un mail
Choix (1-5) :
```

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
