from musique import jouer_musique
import os

def main():

    # Boucle infinie pour afficher en continu
    while True:
        
        choix = input("Que veux-tu faire ? (musique / quit) : ").lower()
        if choix == "musique":
            fichier = input("Nom du fichier audio: ")
            chemin = os.path.join("musique", fichier)
            jouer_musique(chemin)

        # Option pour quitter
        elif choix == "quit":
            print("A bientôt !")
            break

        # Si l'utilisateur entre une commande inconnue
        else:
            print("ERROR : Commande valide : 'musique' ou 'quit'.")

if __name__ == "__main__":
    main()