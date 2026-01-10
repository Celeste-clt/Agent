import os


def creer_fichier(nom_fichier):
    if os.path.exists(nom_fichier):
        print("Le fichier existe déjà.")
        return

    contenu = input("Écris le contenu du fichier :\n")

    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(contenu)

    print(f"Fichier '{nom_fichier}' créé.")


def modifier_fichier(nom_fichier):
    if not os.path.exists(nom_fichier):
        print("Le fichier n'existe pas.")
        return

    contenu = input("Nouveau contenu du fichier :\n")

    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(contenu)

    print(f"Fichier '{nom_fichier}' modifié.")


def supprimer_fichier(nom_fichier):
    if not os.path.exists(nom_fichier):
        print("Le fichier n'existe pas.")
        return

    os.remove(nom_fichier)
    print(f"Fichier '{nom_fichier}' supprimé.")
