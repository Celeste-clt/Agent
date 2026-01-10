from music import jouer_musique
from add import creer_fichier, modifier_fichier, supprimer_fichier
from agenda import ajouter_evenement
from mail import creer_mail

import os

def analyser_phrase(phrase):
    phrase = phrase.lower()
    
    # musique
    if "joue" in phrase or "musique" in phrase:
        fichier = input("Quel fichier audio ? (ex: travis.mp3) : ")
        chemin = os.path.join("musique", fichier)
        jouer_musique(chemin)

    # mail (en json)
    elif "mail" in phrase or "email" in phrase:
        destinataire = input("Destinataire : ")
        sujet = input("Sujet : ")
        contenu = input("Contenu : ")

        creer_mail(destinataire, sujet, contenu)

    # file
    elif "crée" in phrase or "creer" in phrase or "fichier" in phrase or "ajoute" in phrase:
        nom = input("Nom du fichier à créer (ex: test.txt) : ")
        creer_fichier(nom)


    # edit
    elif "modifie" in phrase or "modifier" in phrase:
        nom = input("Nom du fichier à modifier : ")
        modifier_fichier(nom)

    # delete
    elif "supprime" in phrase or "supprimer" in phrase or "supprime" in phrase:
        nom = input("Nom du fichier à supprimer : ")
        supprimer_fichier(nom)


    elif "événement" in phrase or "evenement" in phrase or "calendrier" in phrase:
        date = input("Date de l'événement (JJ/MM/AAAA) : ")
        lieu = input("Lieu : ")
        titre = input("Titre : ")

        ajouter_evenement(date, lieu, titre) 


    # quit
    elif "quit" in phrase or "quitte" in phrase:
        print("À bientôt !")
        return False

    else:
        print("Je n'ai pas compris la demande.")

    return True


def main():
    print("🤖 Agent lancé. Je t'écoute !")

    while True:
        phrase = input("> ")
        if not analyser_phrase(phrase):
            break

if __name__ == "__main__":
    main()
