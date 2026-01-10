from musique import jouer_musique
from add import creer_fichier, modifier_fichier, supprimer_fichier
import os

def analyser_phrase(phrase):
    phrase = phrase.lower()

    # music
    if "joue" in phrase or "musique" in phrase:
        fichier = input("Quel fichier audio ? (ex: travis.mp3) : ")
        chemin = os.path.join("musique", fichier)
        jouer_musique(chemin)

    # file
    elif "crée" in phrase or "creer" in phrase:
        nom = input("Nom du fichier à créer (ex: test.txt) : ")
        creer_fichier(nom)

    # edit
    elif "modifie" in phrase or "modifier" in phrase:
        nom = input("Nom du fichier à modifier : ")
        modifier_fichier(nom)

    # delete
    elif "supprime" in phrase or "supprimer" in phrase:
        nom = input("Nom du fichier à supprimer : ")
        supprimer_fichier(nom)

    # quit
    elif "quit" in phrase or "quitte" in phrase:
        print("À bientôt !")
        return False

    else:
        print("Je n'ai pas compris la demande.")

    return True


def main():
    print("Agent lancé. Je t'écoute !")

    while True:
        phrase = input("> ")

        continuer = analyser_phrase(phrase)
        if not continuer:
            break


if __name__ == "__main__":
    main()
