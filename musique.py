import os

def jouer_musique(nom_fichier):
    """Lance une musique depuis le terminal"""
    if os.path.exists(nom_fichier):
        print(f"Lancement de {nom_fichier}...")
        if os.name == "nt":
            os.system(f"start {nom_fichier}")
        elif os.uname().sysname == "Darwin":
            os.system(f"open {nom_fichier}")
        else:
            os.system(f"xdg-open {nom_fichier}")
    else:
        print("Fichier non trouvé.")
